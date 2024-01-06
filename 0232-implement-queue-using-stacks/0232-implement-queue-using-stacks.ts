class MyQueue {
    stack1:number[];
    constructor() {
        this.stack1=[];
    }

    push(x: number): void {
        this.stack1.push(x);
    }

    pop(): number {
        let stack2=[];
        while(this.stack1.length>0){
            stack2.push(this.stack1.pop());
        }
        let result=stack2.pop();
        while(stack2.length>0){
            this.stack1.push(stack2.pop());
        }

        return result
    }

    peek(): number {
        return this.stack1[0];
    }

    empty(): boolean {
        return this.stack1.length==0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */