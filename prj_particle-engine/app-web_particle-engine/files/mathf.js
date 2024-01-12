class Color {
    constructor(_color = "#000000") {
        this.color = Color.CalculateLenght(_color);
        this.vector = Color.ColorToVector(this.color);
    }

    static CalculateLenght(color = "#000") {
        if (color.length === 4)
            return "#" + color[1] + color[1] + color[2] + color[2] + color[3] + color[3];
        else if (color.length === 7)
            return color
        else
            console.error("This constructor accept only #*** or #****** colors");
    }

    static TwoDigits(num="00") {
        if (num.length == 2) return num;
        else if (num.length == 1) return "0" + num;
        else console.error(num, "something went wrong!");
    }

    static ColorToVector(color = "#000000") {
        let vector = [];
        vector.push(parseInt(color.slice(1,3),16));
        vector.push(parseInt(color.slice(3,5),16));
        vector.push(parseInt(color.slice(5,7),16));
        return vector;
    }

    static VectorToColor(vector) {
        let newString = "#";
        for (let i = 0; i < vector.length; i++)
            newString += Color.TwoDigits(vector[i].toString(16));
        return newString;
    }

    static ColorLerp(minColor = new Color("#000000"), maxColor = new Color("#FFFFFF"), fact = .5) {
        let minVector = minColor.vector;        
        let maxVector = maxColor.vector;
        
        let newVector = []
        newVector.push(Color.TwoDigits(Math.round(Mathf.Lerp(minVector[0], maxVector[0], fact)).toString(16)));
        newVector.push(Color.TwoDigits(Math.round(Mathf.Lerp(minVector[1], maxVector[1], fact)).toString(16)));
        newVector.push(Color.TwoDigits(Math.round(Mathf.Lerp(minVector[2], maxVector[2], fact)).toString(16)));

        return Color.VectorToColor(newVector);
    }

    static Complementary(color = new Color("#FFFFFF")) {
        let newVector = [];
        for (let i = 0; i < color.vector.length; i++)
            newVector.push(255 - color.vector[i]);
        return Color.VectorToColor(newVector);
    }
}

class Mathf {
    static Clamp(value = 0, min = 0, max = 0) {
        if (value < min)
            value = min;
        if (value > max)
            value = max;
        return value;
    }

    static CircularClamp(val, min, max) {
        if (val >= max)
            val = min + (val - max);
        else if (val < min)
            val = max - (min - val);
        return val;
    }

    static RandomInt(min = 0, max = 0) {
        return Math.floor(Math.random() * (max - min) + min);
    }
    
    static Lerp(min = 0, max = 0, fact = 0) {
        fact = Mathf.Clamp(fact, 0, 1);
        let a = max - min;
        let b = a * fact;
        return min + b;
    }

    static Flip(num=0) {
        return 1 - num;
    }

    static EaseIn(num=0, power=2) {
        return Math.pow(num, power);
    }

    static EaseOut(num=0) {
        return Mathf.Flip(Math.sqrt(Mathf.Flip(num)));
    }

    static Spike(num=0) {
        if (num <= .5) return Mathf.EaseIn(num/.5);
        return Mathf.EaseIn(Mathf.Flip(num)/.5);
    }
    
}

class Vector2 {
    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    Magnitude() {
        return Vector2.Distance(new Vector2(0,0), new Vector2(this.x,this.y));
    }

    Round() {
        this.x = Math.round(this.x);
        this.y = Math.round(this.y);
        return this;
    }

    static Distance(point1 = new Vector2(0,0), point2 = new Vector2(0,0)) {
        return Math.sqrt(Math.pow(point2.x - point1.x, 2) + Math.pow(point2.y - point1.y, 2));
    }

    static Subtract(v1 = new Vector2(0,0), v2 = new Vector2(0,0)) {
        return new Vector2(v1.x-v2.x, v1.y-v2.y);
    }
}

class Utility {
    static Wait = async (sec=0, callback) => {
        await new Promise(r => setTimeout(callback, sec * 1000));
    }

    static DelayLoopEqual = async (steps=0, sec=0, callback, skip=()=>{return false;}) => {
        for (let i = 0; i <= steps ; i++) {
            if (skip(i)) continue;
            await new Promise(resolve => setTimeout(resolve, sec * 1000));
            callback(i);
        }
    }

    static DelayLoop = async (steps=0, sec=0, callback, skip=()=>{return false;}) => {
        for (let i = 0; i < steps ; i++) {
            if (skip(i)) continue;
            await new Promise(resolve => setTimeout(resolve, sec * 1000));
            callback(i);
        }
    }

    static TogleClass(_element=new Image(), _class="") {
        if (_element.classList.contains(_class)) _element.classList.remove(_class);
        else _element.classList.add(_class);
    }

}
