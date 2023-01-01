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
    child.cloneNode();
    child.setAttribute("x", "-50");
    child.setAttribute("y", "-50");
    child.setAttribute("width", "200");
    child.setAttribute("height", "200");
    root.appendChild(child);
}

main();
