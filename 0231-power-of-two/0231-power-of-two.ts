function isPowerOfTwo(n: number): boolean {
    let result=Math.log(n)/Math.log(2);
    return result%1<1e-10;
};