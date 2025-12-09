use std::cmp::max;
use std::collections::HashSet;
use std::collections::HashMap;
use std::fs;

fn main() {
    let contents = fs::read_to_string("src/bin/day9/data.txt")
        .expect("Should have been able to read the file");

    let mut rows: usize = 0;
    let mut cols: usize = 0;
    let mut points: Vec<Vec<usize>> = Vec::new();

    for line in contents.lines() {
        let point: Vec<usize> = line.split(',').map(str::trim).map(str::parse::<usize>).collect::<Result<Vec<usize>, _>>().unwrap();
        points.push(vec![point[0], point[1]]);
    }

    for p in points.iter() {
        rows = max(rows, p[0] + 2);
        cols = max(cols, p[1] + 2);
    }

    fn point_on_segment(px: f64, py: f64, x1: f64, y1: f64, x2: f64, y2: f64) -> bool {
        let cross: f64 = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1);
        if cross.abs() > 1e-9 {
            return false;
        }

        let min_x = x1.min(x2);
        let max_x = x1.max(x2);
        let min_y = y1.min(y2);
        let max_y = y1.max(y2);

        px >= min_x - 1e-9
            && px <= max_x + 1e-9
            && py >= min_y - 1e-9
            && py <= max_y + 1e-9
    }

    fn point_in_loop(px: f64, py: f64, points: &[Vec<usize>]) -> bool {
        let n: usize = points.len();
        let mut inside: bool = false;

        for i in 0..n {
            let p1: &Vec<usize> = &points[i];
            let p2: &Vec<usize> = &points[(i + 1) % n];
            let x1 = p1[0] as f64;
            let y1 = p1[1] as f64;
            let x2 = p2[0] as f64;
            let y2 = p2[1] as f64;

            if point_on_segment(px, py, x1, y1, x2, y2) {
                return true;
            }

            let intersects: bool = (y1 > py) != (y2 > py);
            if intersects {
                let x_intersect: f64 = x1 + (py - y1) * (x2 - x1) / (y2 - y1);
                if x_intersect > px {
                    inside = !inside;
                }
            }
        }

        inside
    }

    fn compress_coords(points: &[Vec<usize>]) -> (Vec<i64>, Vec<i64>, Vec<Vec<bool>>) {
        let mut xs: Vec<i64> = points.iter().map(|p: &Vec<usize>| p[0] as i64).collect();
        let mut ys: Vec<i64> = points.iter().map(|p: &Vec<usize>| p[1] as i64).collect();
        xs.sort();
        xs.dedup();
        ys.sort();
        ys.dedup();

        let w: usize = xs.len() - 1;
        let h: usize = ys.len() - 1;

        let mut inside: Vec<Vec<bool>> = vec![vec![false; w]; h];

        for j in 0..h {
            for i in 0..w {
                let cx: f64 = (xs[i] + xs[i + 1]) as f64 * 0.5;
                let cy: f64 = (ys[j] + ys[j + 1]) as f64 * 0.5;
                inside[j][i] = point_in_loop(cx, cy, points);
            }
        }

        (xs, ys, inside)
    }

    fn calc_max_area(xs: &[i64], ys: &[i64], inside: &[Vec<bool>], points_set: &HashSet<(i64, i64)>) -> i64 {
    
        let x_to_idx: HashMap<i64, usize> = xs.iter().enumerate().map(|(i, &x)| (x, i)).collect();
        let y_to_idx: HashMap<i64, usize> = ys.iter().enumerate().map(|(j, &y)| (y, j)).collect();
    
        let mut max_area: i64 = 0;
        
        for &(x1, y1) in points_set.iter() {
            for &(x2, y2) in points_set.iter() {
                if (x1, y1) >= (x2, y2) { continue; }
                
                if x1 == x2 || y1 == y2 {
                    continue;
                }
    
                let x_l = x1.min(x2);
                let x_r = x1.max(x2);
                let y_b = y1.min(y2);
                let y_t = y1.max(y2);
    
                let &i_l = x_to_idx.get(&x_l).unwrap();
                let &i_r = x_to_idx.get(&x_r).unwrap();
                let &j_b = y_to_idx.get(&y_b).unwrap();
                let &j_t = y_to_idx.get(&y_t).unwrap();
    
                if (j_b..j_t).all(|j| (i_l..i_r).all(|i| inside[j][i])) {
                    let area = (x_r - x_l + 1) * (y_t - y_b + 1);
                    max_area = max_area.max(area);
                }
            }
        }
        max_area
    }

    let (xs, ys, inside) = compress_coords(&points);
    let points_set: HashSet<(i64, i64)> = points.iter().map(|p| (p[0] as i64, p[1] as i64)).collect();
    let max_area: i64 = calc_max_area(&xs, &ys, &inside, &points_set);
    println!("{}", max_area);
}
