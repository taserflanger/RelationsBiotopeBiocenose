class Grid {
    constructor(size) {
        this.size = size
        this.case_size = 20
        this.rectanglesOrigins = []
        this.propsList = new Array(this.size**2)
        for (let i = 0; i < this.propsList.length; i++) {
            this.propsList[i] = {"plant":0, "salinity": Math.random()*100, "water": Math.random()*100, "sunshine": Math.random()*100}
        }
        this.textures = ["plant", "salinity", "sunshine", "water"]
        this.texturesRanges = {"plant": [0, 1],"salinity": [0, 100], "sunshine": [0, 100], "water": [0, 100]}

    }
    draw() {
        return null
    }

    setRects() {
        for (x=0; x<this.size; x++) {
            for (var y = 0; y < this.size; y++) {
                this.rectangles.push(x*case_size, y*case_size)
            }
        }
    }
    softmax(vals) {
        let exps = new Array(vals.length)
        let sum = 0
        for (let val in vals) {
            let e = Math.exp(vals[val]/sensor.value())
            exps[val] = e
            sum += e
        }
        for (val in exps) {
            exps[val]/=sum
        }
        return exps
    }

    getTextureOpacities() {
        function operateArrays(arrayA, arrayB, fn){
            if(arrayA.length!==arrayB.length) throw new Error("Cannot operate arrays of different lengths");
            return arrayB.map(function(b, i){
                return fn(arrayA[i], b)
            })
        }
        let cases = new Array(this.size**2)
        let ranges = []
        for (let r in this.texturesRanges) {
            ranges.push(this.texturesRanges[r][1]-this.texturesRanges[r][0])
        }
        for (let c in cases) {
            let values = new Array(this.textures.length)
            for (let p in this.propsList[c]) {
                values[p] = this.propsList[c][p]
            }
            let vals = operateArrays(ranges, values, (a, b)=> {
                return a * b
            })
            let exps = softmax(vals)
            console.log(exps)
            
            cases.push(exps)
        }
        return cases
    }

    setProps(x, y, new_props) {
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