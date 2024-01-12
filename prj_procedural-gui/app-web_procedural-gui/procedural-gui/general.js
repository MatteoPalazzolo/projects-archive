function togle_class(elem, cls="") {
    if (elem.classList.contains(cls)) {
        elem.classList.remove(cls);
        return false;
    }
    else {
        elem.classList.add(cls);
        return true;
    }
}

function clamp(value = 0, min = 0, max = 0) {
    if (value < min)
        value = min;
    if (value > max)
        value = max;
    return value;
}