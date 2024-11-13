var maxProfitAssignment = function(difficulty, profit, worker) {
    let res = 0;
    // The relationship between difficulty and profit
    let map = new Map();
    for(let i=0; i<difficulty.length; i++){
        if(map.has(difficulty[i])){
            let p = map.get(difficulty[i]);
            p = profit[i] > p ? profit[i] : p;
            map.set(difficulty[i], p);
        }else{
            map.set(difficulty[i], profit[i]);
        }
    }
    // sort from small to big
    difficulty.sort((a, b) => a-b);
    worker.sort((a, b) => a-b);
    
    let sum = 0;
    let index = 0;
    for(let i=0; i<worker.length; i++){
        while(worker[i] >= difficulty[index]){
            let p = map.get(difficulty[index]);
            if(p > sum){
                sum = p;
            }
            index ++;
        }
        res += sum;
    }

    return res;    
};