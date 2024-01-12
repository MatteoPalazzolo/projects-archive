/************ CLASSES ************/
let objectsList = [];
let emptySpaces = [];
let entity = 0;
let frameNum = 0;

class Entity {
    constructor(_pos = new Vector2()) {
        entity++;
        this.frame = frameNum;
        this.pos = _pos.Round();
        this.index = this.FindEmptySlot();
    }

    FindEmptySlot() {
        if (emptySpaces.length > 0)
            return emptySpaces.shift();
        objectsList.push(this);
        return objectsList.length-1;
    }
}

class Sand extends Entity {
    static type = 1;
    constructor(_pos = new Vector2()) {
        super(_pos);
    }

    Update() {
        this.FlowSand();
        this.Draw();
    }
    
    FlowSand() {
        let lastPos = undefined;
        
        let nextY = BoundY(this.pos.y + 1);
        let checkRight = granesMatrix[BoundX(this.pos.x + 1)][this.pos.y] === emptyChar;
        let checkLeft = granesMatrix[BoundX(this.pos.x - 1)][this.pos.y] === emptyChar;
        if (granesMatrix[BoundX(this.pos.x)][nextY] === emptyChar) {
            lastPos = new Vector2(this.pos.x, this.pos.y);
            this.pos.y += 1;
        }
        else if (granesMatrix[BoundX(this.pos.x + 1)][nextY] === emptyChar && checkRight) {
            lastPos = new Vector2(this.pos.x, this.pos.y);
            this.pos.x += 1;
            this.pos.y += 1;
        }
        else if (granesMatrix[BoundX(this.pos.x - 1)][nextY] === emptyChar  && checkLeft) {
            lastPos = new Vector2(this.pos.x, this.pos.y);
            this.pos.x -= 1;
            this.pos.y += 1;
        }
        if (lastPos != undefined)
            ErasePixel(new Vector2(lastPos.x, lastPos.y));
    }

    Draw() {
        granesMatrix[BoundX(this.pos.x)][BoundY(this.pos.y)] = this.index;
        DrawPixel(new Vector2(this.pos.x, this.pos.y), this.GetColorByFrame());
    }

    /* deprecated */
    GetColorByAbove() { /* too computation */
        let above = 0;
        for (let i = 0; i < granesMatrix[this.pos.x].length; i++) {
            if (objectsList[granesMatrix[this.pos.x][i]]?.constructor.type === Sand.type && i < this.pos.y) above++;
            if (above >= 10) break;
        } 
        return new Color(Color.ColorLerp(SNOW_COLOR, ICE_COLOR, above/10));
    }

    GetColorByFrame() {
        let deltaFrame = frameNum - this.frame;
        return new Color(Color.ColorLerp(SNOW_COLOR, ICE_COLOR, deltaFrame/1200));
    }    
}

class Dirt extends Entity {
    static type = 2;
    constructor(_pos = new Vector2()) {
        super(_pos);
    }

    Update() {
        this.Draw();
    }

    Draw() {
        granesMatrix[BoundX(this.pos.x)][BoundY(this.pos.y)] = this.index;
        DrawPixel(new Vector2(this.pos.x, this.pos.y), new Color("#692F15"));
    }
}

function BoundX(x) {
    return Mathf.Clamp(x, 0, canvasSize.x - 1);
}

function BoundY(y) {
    return Mathf.Clamp(y, 0, canvasSize.y - 1);
}