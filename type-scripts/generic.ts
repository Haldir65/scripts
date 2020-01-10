// function createArray(length:number, value:number):Array<any> {
//  let result = [];
//  for(let i = 0; i< length ; i++) {
//      result.push[value];
//  }
//  return result;
// }


let param = [3, 4]
// createArray(...param);
var numbers = [1, 2, 3, 4, 5];

console.log(...numbers); 


function createArray<T>(length: number, value: T): Array<T> {
    let result: T[] = [];
    for (let i = 0; i < length; i++) {
        result[i] = value;
    }
    return result;
}

let arr = createArray<string>(3, 'x'); // ['x', 'x', 'x']


console.log(...arr)

function swap<T, U>(tuple: [T, U]): [U, T] {
    return [tuple[1], tuple[0]];
}

swap([7, 'seven']); // ['seven', 7]

interface Lengthwise {
    length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
    console.log(arg.length);
    return arg;
}

loggingIdentity([7,9]);


function copyFields<T extends U, U>(target: T, source: U): T {
    for (let id in source) {
        target[id] = (<T>source)[id];
    }
    return target;
}

// let x :Map<string,number>= new Map<string,number>()

let y :Map<number,number> = new Map([[1,1],[2,2]])


let x = { a: 1, b: 2, c: 3, d: 4 };

copyFields(x, { b: 10, d: 20 });




function logMapElements(value:number, key:number, map:Map<number,number>) {
    console.log("m[" + key + "] = " + value);
}

y.forEach(logMapElements)