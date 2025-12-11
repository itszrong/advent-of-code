use std::fs;
use good_lp::{
    variables, variable, Expression, Solution, SolverModel,
    constraint, lp_solve,
};

fn get_n(line: &str) -> usize {
    let elements = line.split_whitespace().collect::<Vec<_>>();

    let joltage_str: &str = elements[elements.len() - 1];
    let joltage_str_vec: Vec<&str> =
        joltage_str[1..joltage_str.len() - 1].split(',').collect();
    let joltage_vec: Vec<usize> = joltage_str_vec
        .iter()
        .map(|x| x.parse::<usize>().unwrap())
        .collect();

    let all_ops: Vec<&str> = elements[1..elements.len() - 1].to_vec();
    let num_buttons = all_ops.len();
    let num_counters = joltage_vec.len();

    let mut ops_vec: Vec<Vec<usize>> = vec![vec![0; num_counters]; num_buttons];
    for (b, op) in all_ops.into_iter().enumerate() {
        let op_vec: Vec<usize> = op[1..op.len() - 1]
            .split(',')
            .map(|x| x.parse::<usize>().unwrap())
            .collect();
        for op_j in op_vec {
            ops_vec[b][op_j] += 1;
        }
    }

    let mut vars = variables!();
    let presses: Vec<_> = (0..num_buttons)
        .map(|_| vars.add(variable().integer().min(0)))
        .collect();

    let objective: Expression = presses.iter().cloned().sum();
    let mut problem = vars.minimise(objective).using(lp_solve);

    for i in 0..num_counters {
        let mut expr = Expression::from(0.0);
        for b in 0..num_buttons {
            let coeff = ops_vec[b][i] as f64;
            if coeff != 0.0 {
                expr = expr + presses[b] * coeff;
            }
        }
        problem = problem.with(constraint!(expr == joltage_vec[i] as f64));
    }

    let solution = problem.solve().unwrap();
    presses
        .iter()
        .map(|v| solution.value(*v).round() as usize)
        .sum()
}

fn main() {
    let contents = fs::read_to_string("src/bin/day10/data.txt")
        .expect("Should have been able to read the file");

    let mut res: usize = 0;
    for line in contents.lines() {
        let n = get_n(line);
        res += n;
    }
    println!("{res}");
}
