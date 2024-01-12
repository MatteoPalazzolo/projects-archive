/************ PARAMS ************/
const CANVAS_SCALE = new Vector2(2, 2);
const FPS = 60;
const emptyChar = -1;

/*** colors ***/
const SAND_COLOR = new Color("#ffff00");
const SNOW_COLOR = new Color("#fff");
const ICE_COLOR = new Color("#8decf5");

let entityClassList = [
    undefined,
    Sand,
    Dirt
];

/************ TO SERIALIZE ************/
const s_run = [true];
const s_mode = ["rain"];
const s_particleType = [1];
const s_brushSize = [10];
const s_brushType = ["circle"];

/************ REF ************/
let fps_counter;
let entity_counter;

let canvas;
let ctx;
let canvasSize;


/************ STATES ************/
let granesMatrix = [];


/********************* BUILD GUI */
function build_GUI() {
    const drop1 = new Array(3);
    drop1[0] = GUI.Dropdown("run", [
        GUI.Checkbox("run?", s_run)
    ]);
    drop1[1] = GUI.Dropdown("meteo", [
    ]);
    drop1[2] = GUI.Dropdown("brush", [
        GUI.Slider("size", s_brushSize, 1, 20),
        GUI.Spinner("type", s_brushType, ["circle","square"]),
        GUI.Spinner("mode", s_mode, ["rain","hill","hourglass"]),
        GUI.BoxSpinner("particle type", s_particleType, [
            GUI.Card("none", 0, "GUI\\images\\sand-icon.jpg"),
            GUI.Card("snow", 1, "GUI\\images\\sand-icon.jpg"),
            GUI.Card("dirt", 2, "GUI\\images\\sand-icon.jpg")
        ])
    ]);

    const tabs = new Array(3);
    tabs[0] = GUI.Tab("main",drop1);
    tabs[1] = GUI.Tab("tab2",[]);
    tabs[2] = GUI.Tab("tab3",[]);

    GUI.Menu(tabs, document.body);
}

/************ FUNCTIONS ************/
function DrawPixel(_pos = new Vector2(0,0), _color = new Color("#000")) {
    ctx.fillStyle = _color.color;
    ctx.fillRect(_pos.x, _pos.y, 1, 1);
}

function ErasePixel(_pos = new Vector2()) {
    ctx.clearRect(_pos.x, _pos.y, 1, 1);
    granesMatrix[_pos.x][_pos.y] = emptyChar;
}

function DestroyParticle(_pos = new Vector2()) {
    let index = granesMatrix[_pos.x][_pos.y];
    if (index != emptyChar) {
        entity--;
        objectsList[index] = 0;
        emptySpaces.push(index);
        ErasePixel(_pos);
    }
}

function BuildEmptyArray(_sizeX, _sizeY) {
    let arr = [];
    for (let i = 0; i < _sizeX; i++) {
        arr.push([]);
    }  
    for (let i = 0; i < _sizeX; i++) {
        for (let j = 0; j < _sizeY; j++) {
            arr[i].push(emptyChar);
        }
    }
    return arr;
}

/************ LOAD ************/
window.addEventListener("load", () => {
    build_GUI();

    fps_counter = document.querySelector("#fps-counter");
    entity_counter = document.querySelector("#entity-counter");
    canvas = document.querySelector("#display");
    canvas.width = 1080/2;
    canvas.height = 1080/2;
    
    ctx = canvas.getContext("2d");
    ctx.scale(CANVAS_SCALE.x, CANVAS_SCALE.y);

    canvasSize = new Vector2(Math.floor(canvas.width / CANVAS_SCALE.x) + 1, Math.floor(canvas.height / CANVAS_SCALE.y) + 1);

    granesMatrix = BuildEmptyArray(canvasSize.x, canvasSize.y-1);
/*
    ctx.fillStyle = BACKGROUND_COLOR.color;
    ctx.fillRect(0, 0, ref_canvas.width, ref_canvas.height);
*/
    SetDrawing();
    Animate();
})

let frameTime = 1000 / FPS;
let startTime, now, then, elapsed;
function Animate() {
    then = Date.now();
    startTime = then;
    CheckFrameRate();
}

function CheckFrameRate() {
    requestAnimationFrame(CheckFrameRate);
    now = Date.now();
    elapsed = now - then;
    if (elapsed > frameTime) {
        then = now - (elapsed % frameTime);
        if (s_run[0]) frameNum++;
        Update();
        if (s_run[0]) objectsList.forEach(obj => {if (obj != 0) obj.Update();});
    }
}


/************ UPDATE ************/
let n = 0;
function Update() {    
    SetMode();
    DrawUpdate();
    UpdateGUI();
}

function SetMode() {
    if (!s_run[0]) return;
    let posX = canvasSize.x-1;
    if (s_mode[0] === "rain") {
        for (let i = 0; i < 2; i++) DrawElement(new Vector2(Mathf.RandomInt(0, posX), 0), Sand.type);
    }
    else if (s_mode[0] === "hill") {
        DrawElement(new Vector2(Mathf.Flip(Mathf.EaseOut(Math.random())) * posX, 0), Sand.type);
    }
    else if (s_mode[0] === "hourglass") {
        n++;
        if (n % 1 === 0) {
            for (let i = 0; i < 1; i++) {
                DrawElement(new Vector2(posX / 2, 0), Sand.type);
            }
        }   
    }
}

function DrawUpdate() {
    if (drawing) {
        if (ctrlDown) EraseElement(mousePos, s_brushSize[0], s_brushType[0]);
        else DrawElement(mousePos, s_particleType[0], s_brushSize[0], s_brushType[0]);
    }
}

function UpdateGUI() {
    if (s_run[0]) {
        entity_counter.innerHTML = "ENTITY: " + entity;
        fps_counter.innerHTML = "TIME: " + frameNum;
    }
}


/************ DRAW ************/
let drawing = false;
let event;
let mousePos;

let mouseDown = 0;
let ctrlDown = false;

function SetDrawing() {
    canvas.addEventListener("pointerdown", e => {
        mouseDown = e.which;
        ctrlDown = e.ctrlKey;
        if (mouseDown === 1) {drawing = true;}
    });
    canvas.addEventListener("pointerup", e => {
        mouseDown = undefined;
        ctrlDown = false;
        if (e.which === 1) {drawing = false;}
        if (e.which === 3) {
            console.log(objectsList[granesMatrix[mousePos.x][mousePos.y]]);
        }
    });
    canvas.addEventListener("pointermove", e => {mousePos = GetMousePos(e);});
    canvas.addEventListener("pointerover", e => {ctrlDown = false;});
}

function GetMousePos(evt) {
    let rect = canvas.getBoundingClientRect();
    let out = new Vector2((evt.clientX - rect.left) / CANVAS_SCALE.x,
                          (evt.clientY - rect.top) / CANVAS_SCALE.y);
    return out.Round();
}

function DrawElement(pos = new Vector2(), index, _brushSize = 1, _brusType = "square") {
    let particleClass = entityClassList[index];
    if (_brushSize === 1) {
        new particleClass(pos);
        return;
    }    
    let radius = _brushSize - 1;
    for (let i = -radius; i <= radius; i++) {
        for (let j = -radius; j <= radius; j++) {
            let otherPos = new Vector2(BoundX(pos.x + i), BoundY(pos.y + j));
            if (_brusType === "circle" && Math.round(Vector2.Distance(pos, otherPos)) > radius) continue;
            if (objectsList[granesMatrix[otherPos.x][otherPos.y]]?.constructor.type != particleClass.type) {
                DestroyParticle(otherPos);
                ErasePixel(otherPos);
                new particleClass(otherPos);
            }       
        }
    }

}

function EraseElement(pos = new Vector2(), _brushSize = 1, _brusType = "square") {
    if (_brushSize === 1) {ErasePixel(pos); return;}
    
    let radius = _brushSize - 1;    
    for (let i = -radius; i <= radius; i++) {
        for (let j = -radius; j <= radius; j++) {
            let otherPos = new Vector2(Mathf.Clamp(pos.x + i, 0, canvasSize.x - 1), Mathf.Clamp(pos.y + j, 0, canvasSize.y - 1));
            if (_brusType === "circle" && Math.round(Vector2.Distance(pos, otherPos)) > radius) continue;
            DrawPixel(otherPos, new Color("#585858"));
            if (granesMatrix[otherPos.x][otherPos.y] != emptyChar) DestroyParticle(otherPos);
        }
    }
}