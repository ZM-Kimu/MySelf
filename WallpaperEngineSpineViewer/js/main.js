/** This script is modified by zmkimu, source from https://github.com/SaltyAom/akane. */
let canvas
let gl
let shader
let batcher
let mvp = new spine.webgl.Matrix4()
let assetManager
let skeletonRenderer
let animationNow = "I"
let animationState
let bgmController
let isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0
let listeners = new Map()


let lastFrameTime
let spineData

const characterMapping = { shiroko: "LobbyShiroko_multi", serika: "LobbySerika_multi", nonomi: "LobbyNonomi_multi", ayane: "LobbyAyane_multi", hoshino: "LobbyHoshino_multi" }

let BINARY_PATH
let ATLAS_PATH
let BGM_PATH


// Spine states
const START_ANIMATION = "Start_Idle_01"
const IDLE_ANIMATION = "Idle_01"
const DUMMY_STATE = "Dummy"
const EYE_OPEN_STATE = "Look_01_M"
const TOUCH_START = "Pat_01_M"
const TOUCH_START_A = "Pat_01_A"
const TOUCH_END = "PatEnd_01_M"
const TOUCH_END_A = "PatEnd_01_A"
const EYE_ANCHOR = "Touch_Eye"
const HEAD_ANCHOR = "Touch_Point"

// Wallpaper engine default settings
let useHD = false
let character = "shiroko"
let isInteractable = true
let skipOpening = false
let isMirror = false
let customScale = 2.5
let targetFps = 60
let offsetX = 0
let offsetY = 100
let bgmVolume = 0.5

// Wallpaper Engine settings
window.wallpaperPropertyListener = {
	applyUserProperties: (props) => {
		bgmController ? "" : init()
		if (props.scale)
			customScale = props.scale.value
		if (props.targetfps)
			targetFps = props.targetfps.value
		if (props.character) {
			character = props.character.value
			init()
		}
		if (props.useHD)
			useHD = props.useHD.value
		if (props.isinteractable)
			isInteractable = props.isinteractable.value
		if (props.skipopening)
			skipOpening = props.skipopening.value
		if (props.screenoffsetx)
			offsetX = props.screenoffsetx.value * 20
		if (props.screenoffsety)
			offsetY = props.screenoffsety.value * 20
		if (props.bgmvolume)
			bgmController.volume = props.bgmvolume.value
		if (props.usehd) {
			useHD = props.usehd.value
			init()
		}
		if (props.mirror) {
			isMirror = props.mirror.value
		}
	}
}

function init() {
	BINARY_PATH = window.location.protocol === 'file:' ? location.href.replace('/index.html', `/assets/${character}/${characterMapping[character]}.skel`) : `../assets/${character}/${characterMapping[character]}.skel`
	ATLAS_PATH = window.location.protocol === 'file:' ? location.href.replace('/index.html', `/assets/${character}/${useHD ? "HD" : "SD"}/${characterMapping[character]}.atlas`) : `../assets/${character}/${useHD ? "HD" : "SD"}/${characterMapping[character]}.atlas`
	BGM_PATH = window.location.protocol === 'file:' ? location.href.replace('/index.html', "/assets/Theme.ogg") : "../assets/Theme.ogg"
	// Setup canvas and WebGL context. We pass alpha: false to canvas.getContext() so we don't use premultiplied alpha when
	// loading textures. That is handled separately by PolygonBatcher.
	canvas = document.getElementById('canvas')
	canvas.width = window.innerWidth
	canvas.height = window.innerHeight
	canvas.scrollLeft = offsetX * (document.documentElement.scrollWidth - window.screen.width)
	canvas.scrollTop = offsetY * (document.documentElement.scrollHeight - window.screen.height)
	let config = { alpha: useHD }
	gl = canvas.getContext('webgl', config) || canvas.getContext('experimental-webgl', config)
	if (!gl) {
		alert('WebGL is unavailable.')
		return
	}

	if (document.getElementById("bgmController") == null) {
		bgmController = document.createElement("audio")
		bgmController.id = "bgmController"
		bgmController.src = BGM_PATH
		bgmController.loop = true
		bgmController.play()
		document.getElementById("root").appendChild(bgmController)
	}

	// Create a simple shader, mesh, model-view-projection matrix, SkeletonRenderer, and AssetManager.
	shader = spine.webgl.Shader.newTwoColoredTextured(gl)
	batcher = new spine.webgl.PolygonBatcher(gl)
	mvp.ortho2d(0, 0, canvas.width - 1, canvas.height - 1)
	skeletonRenderer = new spine.webgl.SkeletonRenderer(gl)
	assetManager = new spine.webgl.AssetManager(gl)

	// Tell AssetManager to load the resources for each skeleton, including the exported .skel file, the .atlas file and the .png
	// file for the atlas. We then wait until all resources are loaded in the load() method.
	assetManager.loadBinary(BINARY_PATH)
	assetManager.loadTextureAtlas(ATLAS_PATH)

	requestAnimationFrame(load)
}



function load() {
	// Wait until the AssetManager has loaded all resources, then load the skeletons.
	if (assetManager.isLoadingComplete()) {
		spineData = loadSpineData(true) // Some version of spine image is not support premultiplied alpha, re-export it then tick premultiplied alpha option.
		lastFrameTime = Date.now() / 1000
		requestAnimationFrame(render) // Loading is done, call render every frame.
	} else {
		requestAnimationFrame(load)
	}
}

function loadSpineData(premultipliedAlpha) {
	// Load the texture atlas from the AssetManager.
	let atlas = assetManager.get(ATLAS_PATH)

	// Create a AtlasAttachmentLoader that resolves region, mesh, boundingbox and path attachments
	let atlasLoader = new spine.AtlasAttachmentLoader(atlas)

	// Create a SkeletonBinary instance for parsing the .skel file.
	let skeletonBinary = new spine.SkeletonBinary(atlasLoader)

	// Set the scale to apply during parsing, parse the file, and create a new skeleton.
	skeletonBinary.scale = 1
	let skeletonData = skeletonBinary.readSkeletonData(assetManager.get(BINARY_PATH))
	let skeleton = new spine.Skeleton(skeletonData)
	let bounds = calculateSetupPoseBounds(skeleton)

	// Create an AnimationState, and set the initial animation in looping mode.
	let animationStateData = new spine.AnimationStateData(skeleton.data)
	animationStateData.defaultMix = 0.2 // This is necessary if referrence to game linear animation.

	animationStateData.setMix(IDLE_ANIMATION, TOUCH_START_A, 0)

	animationState = new spine.AnimationState(animationStateData)

	if (!skipOpening)
		animationState.addAnimation(0, START_ANIMATION, false)
	animationState.addAnimation(0, IDLE_ANIMATION, true, 0)

	// Horizontal flip for mirroring.
	//if (isMirror)
	//	skeleton.findBone("root").scaleX = -1

	animationState.setEmptyAnimation(1)
	animationState.setEmptyAnimation(2)

	// Get the cursor of touching effect.
	let eyeCursor = skeleton.findBone(EYE_ANCHOR)
	let headCursor = skeleton.findBone(HEAD_ANCHOR)

	if (isInteractable)
		setAnimationCursorEventForStatus(eyeCursor, headCursor)
	//setAnimationEventController(canvas)

	// Pack everything up and return to caller.
	return { skeleton: skeleton, state: animationState, bounds: bounds, premultipliedAlpha: premultipliedAlpha }
}


// Set character as interactable. Can interact it with touch event.
function setAnimationCursorEventForStatus(eyeBone, headBone) {
	// The axios in spine is reversed.
	const headAnchor = { x: headBone.y, y: headBone.x }
	const eyeAnchor = { x: eyeBone.y, y: eyeBone.x }
	let mouseDown = false
	let isMoved = false
	let x
	let y
	let moveX, moveY

	// Mouse down case
	function interactStart(event) {
		if (!mouseDown) {
			headBone.x = headAnchor.y
			headBone.y = headAnchor.x

			if (event.type === 'touchstart') {
				x = event.touches[0].clientX
				y = event.touches[0].clientY
			}
			else {
				x = event.clientX
				y = event.clientY
			}

			if (animationNow == "I")
				animationState.addAnimation(1, DUMMY_STATE, false, 0)

			animationState.setAnimation(1, TOUCH_START, false, 0)
			animationState.setAnimation(2, TOUCH_START_A, false, 0)

			isMoved = false
			mouseDown = true
		}
	}

	// Mouse up case
	function interactEnd(_) {
		if (mouseDown) {
			mouseDown = false

			if (isMoved) {
				// Moved case
				animationState.addAnimation(1, DUMMY_STATE, false, 0)
				animationNow = "I"
			} else {
				// Clicked case
				switch (animationNow) {
					case "I":
						animationNow = "T"
						animationState.addAnimation(1, TOUCH_START, false, 0)
						break
					case "T":
						animationState.addAnimation(1, TOUCH_END, false, 0)
						animationNow = "I"
						break
				}
			}

			animationState.addAnimation(2, TOUCH_END_A, false, 0)
			//animationState.addAnimation(2, DUMMY_STATE, false, 0)
			animationState.addEmptyAnimation(2)

			headBone.x = headAnchor.y
			headBone.y = headAnchor.x
		}
	}

	// Mouse move case
	function interactMove(event) {
		const bone = mouseDown ? headBone : eyeBone
		let touchPointX, touchPointY

		isMoved = mouseDown

		touchPointX = event.x
		touchPointY = event.y
		if (event.type === 'touchmove') {
			touchPointX = event.touches[0].clientX
			touchPointY = event.touches[0].clientY
		}

		if (mouseDown) {
			moveX = (touchPointX - x) * 150 / canvas.width
			moveY = (touchPointY - y) * 150 / canvas.height
			moveX = Math.abs(moveX) >= 30 ? moveX > 0 ? 30 : -30 : moveX
			moveY = Math.abs(moveY) >= 30 ? moveY > 0 ? 30 : -30 : moveY
			moveX = isMirror ? -(moveX + headAnchor.x) : -(headAnchor.x - moveX)
			moveY = -(headAnchor.y - moveY)
		}
		else {
			x = canvas.width / 2
			y = canvas.height / 2
			moveX = ((isMirror ? x - touchPointX : touchPointX - x) / x * 80) - eyeAnchor.x
			moveY = ((touchPointY - y) / y * 80) - eyeAnchor.y
		}

		bone.x = -moveY
		bone.y = -moveX
	}

	addOrRemoveListener(canvas, 'touchstart', interactStart, false)
	addOrRemoveListener(canvas, 'touchmove', interactMove, false)
	addOrRemoveListener(canvas, 'touchend', interactEnd, false)
	addOrRemoveListener(canvas, "mousedown", interactStart, false)
	addOrRemoveListener(canvas, "mousemove", interactMove, false)
	addOrRemoveListener(canvas, "mouseup", interactEnd, false)

}


function addOrRemoveListener(parent, type, callback, option, removeOnly = false) {
	const listener = listeners.get(parent) || {}

	if (listener && listener[type]) {
		parent.removeEventListener(type, listener[type])
		listeners.delete(parent)
	}
	if (!removeOnly) {
		parent.addEventListener(type, callback, option)
		listeners[type] = callback
		listeners.set(parent, listeners)
	}

}



function calculateSetupPoseBounds(skeleton) {
	skeleton.setToSetupPose()
	skeleton.updateWorldTransform()
	let offset = new spine.Vector2()
	let size = new spine.Vector2()
	skeleton.getBounds(offset, size, [])
	return { offset: offset, size: size }
}

function render() {
	let now = Date.now() / 1000
	let delta = now - lastFrameTime
	//let fps = 1 / delta

	lastFrameTime = now

	// Update the MVP matrix to adjust for canvas size changes
	resize()

	gl.clearColor(0.3, 0.3, 0.3, 1)
	gl.clear(gl.COLOR_BUFFER_BIT)

	// Apply the animation state based on the delta time.
	let skeleton = spineData.skeleton
	let state = spineData.state
	let premultipliedAlpha = spineData.premultipliedAlpha
	state.update(delta)
	state.apply(skeleton)
	skeleton.updateWorldTransform()

	// Bind the shader and set the texture and model-view-projection matrix.
	shader.bind()
	shader.setUniformi(spine.webgl.Shader.SAMPLER, 0)
	shader.setUniform4x4f(spine.webgl.Shader.MVP_MATRIX, mvp.values)

	// Start the batch and tell the SkeletonRenderer to render the active skeleton.
	batcher.begin(shader)
	skeletonRenderer.premultipliedAlpha = premultipliedAlpha
	skeletonRenderer.draw(batcher, skeleton)
	batcher.end()

	shader.unbind()

	// throttle fps
	let elapsed = Date.now() / 1000 - now
	let targetFrameTime = 1 / targetFps
	let delay = Math.max(targetFrameTime - elapsed, 0) * 1000

	setTimeout(() => {
		requestAnimationFrame(render)
	}, delay)
}

function resize() {
	let w = canvas.clientWidth
	let h = canvas.clientHeight
	if (canvas.width != w || canvas.height != h) {
		canvas.width = w
		canvas.height = h
	}

	// Calculations to center the skeleton in the canvas.
	let bounds = spineData.bounds
	let centerX = bounds.offset.x + bounds.size.x / 2
	let centerY = bounds.offset.y + bounds.size.y / 2
	let scaleX = bounds.size.x / canvas.width
	let scaleY = bounds.size.y / canvas.height
	let scale = Math.max(scaleX, scaleY) * 1.2
	scale = Math.max(scale, 1)
	scale = scale / customScale
	let width = canvas.width * scale
	let height = canvas.height * scale

	// Horizontal flip for mirroring.
	width = isMirror ? -width : width

	mvp.ortho2d(centerX - width / 2 + offsetX, centerY - height / 2 - offsetY, width, height)
	gl.viewport(0, 0, canvas.width, canvas.height)
}

