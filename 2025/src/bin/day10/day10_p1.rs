use std::fs;
use std::collections::HashSet;
fn main() {

    fn get_n (line: &str) -> usize {

        let elements = line.split_whitespace().collect::<Vec<_>>();
        
        let mut target_str: &str = elements[0];
        target_str = &target_str[1..target_str.len()-1];
        let mut target_vec: Vec<bool> = Vec::new();
        for i in target_str.chars() {
            if i == '.' {
                target_vec.push(false)
            } else {
                target_vec.push(true)
            }
        }
        
        let all_ops: Vec<&str> = elements[1..elements.len()-1].to_vec();
        let mut ops_vec: Vec<Vec<bool>> = vec![vec![false; target_vec.len()]; all_ops.len()];
        for (i, op) in all_ops.into_iter().enumerate() {
            let op_str_vec: Vec<&str> = op[1..op.len()-1].split(',').collect();
            for op_str in op_str_vec.iter() {
                ops_vec[i][op_str.parse::<usize>().unwrap()] = true;
            }
        }

        let mut initial_set: HashSet<Vec<bool>> = HashSet::new();
        let mut prev_sets: Vec<HashSet<Vec<bool>>> = Vec::new();
        initial_set.insert(target_vec.clone());
        prev_sets.push(initial_set);

        if ops_vec.contains(&target_vec) {
            return 1;
        }

        for n in 0..ops_vec.len() {
            let mut new_sets: Vec<HashSet<Vec<bool>>> = Vec::new();
            for prev_set in prev_sets.iter() {
                for curr_op in ops_vec.iter() {
                    let mut prev_set_clone: HashSet<Vec<bool>> = prev_set.clone();
                    if prev_set_clone.contains(curr_op) {
                        continue
                    }
                    prev_set_clone.insert(curr_op.clone());
                    if new_sets.contains(&prev_set_clone) {
                        continue;
                    }
                    let mut xor_value: Vec<bool> =  vec![false; curr_op.len()];
                    for k in prev_set_clone.iter() {
                        xor_value = xor_value.iter().zip(k.iter()).map(|(x, y)| *x ^ *y).collect::<Vec<bool>>();
                    }
                    if ops_vec.contains(&xor_value) {
                        return n+2;
                    }
                    new_sets.push(prev_set_clone.clone());
                }
            }
            prev_sets = new_sets;   
        }
        return ops_vec.len();
    }

    let contents = fs::read_to_string("src/bin/day10/data.txt")
        .expect("Should have been able to read the file");

    let mut res: usize = 0;
    for line in contents.lines() {
        let n = get_n(line);
        println!("{}", n);
        res += n;
    }
    println!("{}", res);
}
