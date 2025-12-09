use std::fs;
use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::BTreeSet;
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

    let mut min_distances: BinaryHeap<Reverse<(i64, usize, usize)>> = BinaryHeap::new();
    let mut graph: HashMap<usize, Vec<usize>> = HashMap::new();
    let no_boxes = contents.lines().count();
    for(i, line1) in contents.lines().enumerate() {
        let coords1 = line1.split(',').map(str::trim).map(str::parse::<i64>).collect::<Result<Vec<_>, _>>().unwrap();
        for(j, line2) in contents.lines().enumerate() {
            if i <= j {
                continue;
            }
            let coords2 = line2.split(',').map(str::trim).map(str::parse::<i64>).collect::<Result<Vec<_>, _>>().unwrap();
            let distance = (coords1[0]-coords2[0]).pow(2)+(coords1[1]-coords2[1]).pow(2)+(coords1[2]-coords2[2]).pow(2);
            min_distances.push(Reverse((distance, i, j)));
        }
    }
    
    let mut pair: (i64, usize, usize) = (0, 0, 0);
    let mut run = true;
    while run {
        let mut visited: BTreeSet<usize> = BTreeSet::new();
        pair = min_distances.pop().unwrap().0;
        graph.entry(pair.1).or_insert(Vec::new()).push(pair.2);
        graph.entry(pair.2).or_insert(Vec::new()).push(pair.1);
        visited = dfs(0, visited, &graph);
        if visited.len() == no_boxes {
            run = false;
        }
    }

    let coord1 = contents.lines().collect::<Vec<_>>()[pair.1];
    let xcoord1 = coord1.split(',').map(str::trim).map(str::parse::<i64>).collect::<Result<Vec<_>, _>>().unwrap()[0];
    let coord2 = contents.lines().collect::<Vec<_>>()[pair.2];
    let xcoord2 = coord2.split(',').map(str::trim).map(str::parse::<i64>).collect::<Result<Vec<_>, _>>().unwrap()[0];
    println!("{}", xcoord1*xcoord2);
}
