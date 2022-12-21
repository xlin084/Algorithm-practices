const arr1 = [33, 22, 55, 33, 11, 33, 5];
const arr2 = [22, 55, 77, 77, 88, 99, 99];

// const intersection = [...new Set(arr1)].filter(x => new Set(arr2).has(x));
const intersection = [...new Set(arr1)].filter((x) => arr2.includes(x));
console.log(intersection);
