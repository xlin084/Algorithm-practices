const arr1 = [33, 22, 55, 33, 11, 33, 5];
const arr2 = [22, 55, 77, 77, 88, 99, 99];

const union = [...new Set([...arr1, ...arr2])];
console.log(union);
