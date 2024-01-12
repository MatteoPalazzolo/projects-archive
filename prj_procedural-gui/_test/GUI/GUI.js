class Utils {
    static clamp(value = 0, min = 0, max = 0) {
        if (value < min)
            value = min;
        if (value > max)
            value = max;
        return value;
    }

    static togle_class(elem, cls="") {
        if (elem.classList.contains(cls)) {
            elem.classList.remove(cls);
            return false;
        }
        else {
            elem.classList.add(cls);
            return true;
        }
    }
}

class GUI {

    static Menu(tabs=[], container=document.body) {
        const gui = document.createElement("div");
        gui.classList.add("GUI");

        const line = document.createElement("div");
        line.classList.add("line");
        
        const content = document.createElement("div");
        content.classList.add("tab-content");

        const tabMenu = document.createElement("div");
        tabMenu.classList.add("tab-menu");
        tabMenu.innerHTML =
        '<div class="content">'+
            '<div class="tabs">'+
            '</div>'+
        '</div>'+
        '<div class="close-bkg">'+
            '<svg class="close" viewBox="0 0 365.696 365.696" xmlns="http://www.w3.org/2000/svg">'+
                '<path d="m243.1875 182.859375 113.132812-113.132813c12.5-12.5 12.5-32.765624 0-45.246093l-15.082031-15.082031c-12.503906-12.503907-32.769531-12.503907-45.25 0l-113.128906 113.128906-113.132813-113.152344c-12.5-12.5-32.765624-12.5-45.246093 0l-15.105469 15.082031c-12.5 12.503907-12.5 32.769531 0 45.25l113.152344 113.152344-113.128906 113.128906c-12.503907 12.503907-12.503907 32.769531 0 45.25l15.082031 15.082031c12.5 12.5 32.765625 12.5 45.246093 0l113.132813-113.132812 113.128906 113.132812c12.503907 12.5 32.769531 12.5 45.25 0l15.082031-15.082031c12.5-12.503906 12.5-32.769531 0-45.25zm0 0"/>'+
            '</svg>'+
        '</div>';

        const close = tabMenu.querySelector(".close-bkg");
        close.addEventListener("click", e => { Utils.togle_class(gui, "close"); });

        create_tabs();

        gui.appendChild(tabMenu);
        gui.appendChild(line);
        gui.appendChild(content);
        container.appendChild(gui);
        load_HTML(0);

        function create_tabs() {
            const tabsContainer = tabMenu.querySelector(".tabs");

            tabs.forEach(tab => {
                const item = document.createElement("div");
                item.classList.add("item");
                const p = document.createElement("p");
                p.innerHTML = tab.label;
                item.appendChild(p);
                tabsContainer.appendChild(item);

                item.addEventListener("click", () => {
                    const items = gui.querySelectorAll(".item");
                    items.forEach(t => {t.classList.remove("selected");});
                    item.classList.add("selected");
                    load_HTML(Array.from(items).indexOf(item));
                });
                tabsContainer.firstChild.classList.add("selected");
            });
        }
        
        function load_HTML(i) {
            while (content.lastChild) content.removeChild(content.lastChild);
            content.appendChild(tabs[i]);
        }
    }

    static Tab(label="", items=[]) {
        const tab = document.createElement("div");
        tab.label = label;
        items.forEach(i => {tab.appendChild(i)});
        return tab;
    }

    static Dropdown(label="", items=[]) {
        const div = document.createElement("div");
        div.classList.add("dropdown");

        const header = document.createElement("div");
        header.classList.add("header");

            const par = document.createElement("p");
            par.innerHTML = label;
            header.appendChild(par);

            const arrow = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            arrow.classList.add("arrow");
            arrow.setAttribute("viewbox","0 0 16 16");

            const arrowPoly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
            arrowPoly.setAttribute("points","1,0 1,16 15,8");
            arrow.appendChild(arrowPoly);

            header.appendChild(arrow);
            
        div.appendChild(header);

        const content = document.createElement("div");
        content.classList.add("content");
        items.forEach(i => {content.appendChild(i)});
        div.appendChild(content);

        header.onclick = () => {Utils.togle_class(div,"open");}

        return div;
    }

    static Slider(label="", varRef=[], min=0, max=0) {
        const div = document.createElement("div");
        div.classList.add("field");
        div.classList.add("slider");

            const span = document.createElement("span");
            span.classList.add("label");
            span.innerHTML = label;
            div.appendChild(span);

            const flexDiv = document.createElement("div");
                const rangeInp = document.createElement("input");
                rangeInp.type = "range";
                rangeInp.min = min;
                rangeInp.max = max;
                rangeInp.value = varRef[0];
                flexDiv.appendChild(rangeInp);

                const textInp = document.createElement("input");
                textInp.type = "text";
                textInp.value = varRef[0];
                flexDiv.appendChild(textInp);

        div.appendChild(flexDiv);

        rangeInp.addEventListener("input", _ => {varRef[0] = textInp.value = rangeInp.value;});
        textInp.addEventListener("keypress", e => {if (e.key == "Enter") set();});
        textInp.addEventListener("focusout", _ => {set()});

        function set() {varRef[0] = textInp.value = rangeInp.value = set_value(textInp.value);}
        function set_value(value) {
            if (isNaN(Number(value))) return Number(min);
            return Utils.clamp(Number(value), Number(min), Number(max));
        }

        return div;
    }

    static Checkbox(label="", varRef=[]) {
        let div = document.createElement("div");
        div.classList.add("field");
        div.classList.add("checkbox");
        div.innerHTML = '<span class="label">'+label+'</span><label class="container"><input type="checkbox"><span class="checkmark"></span></label>';
        const check = div.querySelector("input[type=checkbox]");
        check.checked = varRef[0];
        check.addEventListener("input", () => {varRef[0] = check.checked});
        return div;
    }

    static Spinner(label="", varRef=[], choices=[]) {
        const div = document.createElement("div");
        div.classList.add("field");
        div.classList.add("spinner");
        div.innerHTML = '<span class="label">'+label+'</span>' + '<div class="spin"> <div class="header"> <p class="current"> </p> <svg class="arrow" viewBox="0 0 16 16"> <polygon points="1,0 1,16 15,8"/> </svg> </div> <div class="content"> <div class="list"> </div> </div> </div>';
        
        const current = div.querySelector(".current");
        varRef[0] = choices[0];
        current.innerHTML = choices[0];

        const list = div.querySelector(".list");
        choices.forEach(c => {
            const p = document.createElement("p");
            p.innerHTML = c;
            list.appendChild(p);
        });

        /************** LISTENER - START **************/
        const header = div.querySelector(".header");
        header.onclick = () => {Utils.togle_class(div,"open");}
    
        let hover = false;
        div.addEventListener("mouseover", () => {hover = true;});
        div.addEventListener("mouseleave", () => {hover = false;});
        
        window.addEventListener("click", () => {
            if (!hover) div.classList.remove("open");
        });
    
        const items = div.querySelectorAll(".list > p");
        items.forEach(i => {
            i.addEventListener("click", () => {
                current.innerHTML = i.innerHTML;
                varRef[0] = i.innerHTML;
                div.classList.remove("open");
            });
        });
        /************** LISTENER - END **************/

        return div;
    }

    static BoxSpinner(label="", varRef=[], cards=[]) {
        const div = document.createElement("div");
        div.classList.add("field");
        div.classList.add("box-spinner");
        div.innerHTML = '<span class="label">'+label+'</span><div class="line"></div><div class="content"></div>';
        const content = div.querySelector(".content");
        varRef[0] = cards[0].getAttribute("type");
        cards.forEach(c => {content.appendChild(c)});

        /************** LISTENER - START **************/
        cards.forEach(card => {
            card.addEventListener("click", () => {
                cards.forEach(elm => {elm.classList.remove("selected");});
                card.classList.add("selected");
                varRef[0] = card.getAttribute("type");
            });
        });
        /************** LISTENER - END **************/

        return div;
    }
    
    static Card(label="", src="") {
        const div = document.createElement("div");
        div.classList.add("card");
        div.setAttribute("type",label);
            const img = document.createElement("img");
            img.src = src;
            img.alt = label;
        div.appendChild(img);
        return div;
    }

}