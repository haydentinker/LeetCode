function isPowerOfThree(n: number): boolean {
    if (n<1){
        return false;
    }
    const logBase3 = Math.log(n) / Math.log(3);
    return Math.abs(logBase3 - Math.round(logBase3))<1e-10;
};