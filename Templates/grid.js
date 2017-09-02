class Grid {
    constructor(size) {
        this.size = size
        // Number of line/columns
        this.case_size = 20
        // Size in pixels of each case
        this.rectanglesOrigins = []
        this.setRects()
        // Creates Rectangles Origins => Array of coordinates [[x, y], ...]
        this.propsList = new Array(Math.pow(this.size, 2))
        for (let i = 0; i < this.propsList.length; i++) {
            this.propsList[i] = {"plant":0, "salinity": Math.random()*100, "water": Math.random()*100, "sunshine": Math.random()*100}
        }
        // Object of props for each case [{...}, {...}]
        this.textures = ["plant", "salinity", "sunshine", "water"]
        // Path of textures
        this.texturesRanges = {"plant": [0, 1],"salinity": [0, 100], "sunshine": [0, 100], "water": [0, 100]}
        // Range for each prop {"prop": [min, max]}
    }
    draw() {
        // Still to make
        return null
    }

    setRects() {
        for (let x=0; x<this.size; x++) {
            for (var y = 0; y < this.size; y++) {
                this.rectanglesOrigins.push([x*this.case_size, y*this.case_size])
            }
        }
    }
    softmax(vals) {
        let sensiblility = 1
        let exps = new Array(vals.length)
        let sum = 0
        for (let val in vals) {
            let e = Math.exp(vals[val]/sensiblility)
            exps[val] = e
            sum += e
        }
        for (let val in exps) {
            exps[val]/=sum
        }
        return exps
        // Returns soft max of given inputs (always sum up to 1)
    }

    getTextureOpacities() {
        function operateArrays(arrayA, arrayB, fn){
            if(arrayA.length!==arrayB.length) throw new Error("Cannot operate arrays of different lengths");
            return arrayB.map(function(b, i){
                return fn(arrayA[i], b)
            })
        }
        // Makes operations between two arrays
        let cases = new Array(Math.pow(this.size, 2))
        // array to return. Each element will be the opacity of the corresponding textures
        let ranges = []
        for (let r in this.texturesRanges) {
            ranges.push(this.texturesRanges[r][1]-this.texturesRanges[r][0])
        }
        // array of prop ranges
        for (let c=0; c<cases.length;c++) {
            let values = new Array(this.textures.length)
            let i=0
            for (let p in this.propsList[c]) {
                values[i] = this.propsList[c][p]
                i++
            }
            // Get the values of prop
            let vals = operateArrays(values, ranges, (a, b)=> {
                return a / b
            })
            // Get the ranges*values
            let exps = this.softmax(vals)
            // Make that all the opacities sum up to 1
            
            cases[c] = exps
        }
        return cases
    }

    setProps(x, y, new_props) {
        // Set the props of coordinate x, y to the new_props
        let prop, new_prop;
        let c = this.propsList[x*this.size+y]
        for (prop in c) {
            for (new_prop in new_props) {
                if (prop == new_prop) {
                    c[prop]= new_props[new_prop]
                }
            }
        }
    }
}

let g = new Grid(10)
g.getTextureOpacities()