let tom: [string, number];
tom = ['Tom', 25];
console.log(tom[0])

tom.push('male'); // useless
// tom.push(true);
console.log(tom[0])
console.log(tom[1])
// console.log(tom[2]) in js file , this will run without error


enum Color {Red, Green, Blue = "blue".length};
console.log(`the color is ${Color.Red.toFixed()}`)
console.log(`Green color is ${Color.Green.toFixed()}`)
console.log(`Blue color is ${Color.Blue.toFixed()}`)

declare const enum Directions {
    Up,
    Down,
    Left,
    Right
}

let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right];


function tryOutEnums(direc:Directions){
    switch(direc){
        case Directions.Down:
            console.log("down");
            break;
        case Directions.Up:
            console.log("Up");
            break;
        case Directions.Left:
            console.log("Left");
            break;
        case Directions.Right:
            console.log("Right");
            break;
        default:
            break;
    }
}

tryOutEnums(directions[0])



class Animal {

    constructor(name:any) {
        this.name = name;
    }
    get name() {
        return 'Jack';
    }
    set name(value) {
        console.log('setter: ' + value);
    }

    static num = 42;
    static isAnimal(a:any) {
        return a instanceof Animal;
    }
}



console.log(Animal.num) //42
Animal.num = 100
console.log(Animal.num) //100

export default Animal



