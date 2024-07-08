class AsciiCircle {
    constructor(width, height, radius, thickness) {
        this.width = width;
        this.height = height;
        this.radius = radius;
        this.thickness = thickness;
        this.centerX = Math.floor(width / 2);
        this.centerY = Math.floor(height / 2);
    }

    draw() {
        let output = '';
        for (let y = 0; y < this.height; y++) {
            for (let x = 0; x < this.width; x++) {
                const distance = Math.sqrt((x - this.centerX) ** 2 + (y - this.centerY) ** 2);
                if (this.radius - this.thickness / 2 < distance && distance < this.radius + this.thickness / 2) {
                    output += '.';
                } else {
                    output += '#';
                }
            }
            output += '\n';
        }
        // Draw the circle in console
        console.log(output);

        return output;
    }
}

// Define the parameters
const width = 41;
const height = 41;
const radius = 17.5;  // Radius of the circle
const thickness = 3;  // Thickness of the circle

// Create an instance of AsciiCircle
const circle = new AsciiCircle(width, height, radius, thickness);

// Draw the circle in browser when the document is loaded
document.addEventListener("DOMContentLoaded", function() {
    console.log("circle.js is successfully loaded!");
    const asciiArt = circle.draw();
    document.getElementById("ascii-art").textContent = asciiArt;
});
