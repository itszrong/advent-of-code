use std::fs;
use std::cmp::min;
use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::BTreeSet;
use ordered_float::OrderedFloat;
fn main() {

    fn dfs(i: usize, mut visited: BTreeSet<usize>, graph: &HashMap<usize, Vec<usize>>) -> BTreeSet<usize> {
        if visited.contains(&i) {
            return visited;
        }
        visited.insert(i);
        if let Some(neighbours) = graph.get(&i) {
            for &visiting in neighbours {
                visited = dfs(visiting, visited, graph);
            }
        }
        visited
    }

    let contents = fs::read_to_string("src/bin/day8/data.txt")
        .expect("Should have been able to read the file");

    let n = 1000;
    let mut min_distances: BinaryHeap<Reverse<(OrderedFloat<f64>, usize, usize)>> = BinaryHeap::new();
    let mut graph: HashMap<usize, Vec<usize>> = HashMap::new();
    for(i, line1) in contents.lines().enumerate() {
        let coords1 = line1.split(',').map(str::trim).map(str::parse::<f64>).collect::<Result<Vec<_>, _>>().unwrap();
        for(j, line2) in contents.lines().enumerate() {
            if i <= j {
                continue;
            }
            let coords2 = line2.split(',').map(str::trim).map(str::parse::<f64>).collect::<Result<Vec<_>, _>>().unwrap();
            let distance = ((coords1[0]-coords2[0]).powf(2.0)+(coords1[1]-coords2[1]).powf(2.0)+(coords1[2]-coords2[2]).powf(2.0)).powf(0.5);
            min_distances.push(Reverse((OrderedFloat(distance), i, j)));
        }
    }
    let n = min(min_distances.len(), n);
    for _ in 0..n {
        let pair = min_distances.pop().unwrap().0;
        graph.entry(pair.1).or_insert(Vec::new()).push(pair.2);
        graph.entry(pair.2).or_insert(Vec::new()).push(pair.1);
    }

    let mut sizes: Vec<usize> = Vec::new();
    let mut total_visited: BTreeSet<usize> = BTreeSet::new();
    let mut sets_of_sets_visited: HashSet<BTreeSet<usize>> = HashSet::new();
    for (i, _adj) in &graph {
        if total_visited.contains(i) {
            continue
        }
        let mut visited: BTreeSet<usize> = BTreeSet::new();
        visited = dfs(*i, visited, &graph);
        sizes.push(visited.len());
        sets_of_sets_visited.insert(visited.clone());
        total_visited.extend(visited);
    }
    sizes.sort();
    let mut res = 1;
    for i in 0..3 {
        res *= sizes[sizes.len()-i-1]
    }
    println!("{:?}", res);
}
