console.log("started.");

async function getSVG(): Promise<SVGSVGElement> {
    const svg = await (await fetch('tile.svg')).text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(svg, "image/svg+xml");
    const e = doc.firstChild as Element;
    return e as SVGSVGElement;
}

async function main() {
    const root = document.getElementById("parent")!!;
    console.log(root);
    console.log(root);
    let child = await getSVG();
    const strokeWidth = 2;
    const hexWidth = 200;
    const hexHeight = 115.311 * 1.5;
    const leftPadding = -100 - strokeWidth / 2;
    const topPadding = -100 - strokeWidth / 2;
    for (let y = 0; y < 5; y++) {
        for (let x = 0; x < 9; x++) {
            if (y % 2 == 0) {
                child.setAttribute("x", `${leftPadding + x * (hexWidth - strokeWidth)}`);
            } else {
                child.setAttribute("x", `${leftPadding + (x + 0.5) * (hexWidth - strokeWidth)}`);
            }
            child.setAttribute("y", `${topPadding + y * (hexHeight - strokeWidth)}`);
            child.setAttribute("width", "400");
            child.setAttribute("height", "400");
            root.appendChild(child.cloneNode(true));
        }
    }
}

main();
