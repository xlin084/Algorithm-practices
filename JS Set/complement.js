const arr1 = [33, 22, 55, 33, 11, 33, 5];
const arr2 = [22, 55, 77, 77, 88, 99, 99];

const union = [...new Set([...arr1, ...arr2])];
const intersection = [...new Set(arr1)].filter((x) => arr2.includes(x));
const complement = union.filter((x) => !intersection.includes(x));
