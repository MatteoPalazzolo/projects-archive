(function() {
const sliderValue1 = [5];
const sliderValue2 = [3];
const sliderValue3 = [90];
const checkbox1 = [true];
const spinner1 = [""];
const boxSpinner1 = [""];

window.addEventListener("load", () => {
    const drop1 = GUI.Dropdown("prova", [
        GUI.Slider("value 1", sliderValue1, 0, 10),
        GUI.Slider("value 2", sliderValue2, 0, 5),
        GUI.Slider("value 3", sliderValue3, 50, 100)
    ]);

    const drop2 = GUI.Dropdown("riprova", [
        GUI.Checkbox("check 1", checkbox1),
        GUI.Spinner("spinner 1", spinner1, ["one","two","three"]),
        GUI.BoxSpinner("box spinner 1", boxSpinner1, [
            GUI.Card("card1", "images\\sand-icon.jpg"),
            GUI.Card("card2", "images\\sand-icon.jpg"),
            GUI.Card("card3", "images\\sand-icon.jpg"),
            GUI.Card("card4", "images\\sand-icon.jpg"),
            GUI.Card("card4", "images\\sand-icon.jpg"),
            GUI.Card("card4", "images\\sand-icon.jpg"),
            GUI.Card("card4", "images\\sand-icon.jpg"),
            GUI.Card("card4", "images\\sand-icon.jpg"),
            GUI.Card("card4", "images\\sand-icon.jpg")
        ])
    ]);

    const drop3 = GUI.Dropdown("prova3", [
        GUI.Slider("value 1", sliderValue1, 0, 10),
        GUI.Slider("value 2", sliderValue2, 0, 5),
        GUI.Slider("value 3", sliderValue3, 50, 100)
    ]);

    const mainTab1 = GUI.Tab("tab1", [drop1, drop2, drop3]);
    const mainTab2 = GUI.Tab("tab2", []);
    const mainTab3 = GUI.Tab("tab3", []);

    GUI.Menu([mainTab1,mainTab2,mainTab3], document.body);
});

})();
