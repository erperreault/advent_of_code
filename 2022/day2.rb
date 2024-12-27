input = File.open("input")

vals = {A: 3, B: 0, C: 6, X: 0, Y: 3, Z: 6}
bonus = {X: 1, Y: 2, Z: 3}

# part1_result = input
#   .read
#   .split("\n")
#   .map {|m| m.split(" ")}
#   .map {|m| m.map {|i| i.to_sym}}
#   .map {|m| ((vals[m[0]] + vals[m[1]]) % 9) + bonus[m[1]]}
#   .sum
# puts "part1: #{part1_result}"

part2 = {X: 0, Y: 3, Z: 6}
part2_opponent = [:A, :B, :C]
part2_bonus = {A: 0, B: 1, C: 2}
adj = {X: 2, Y: 0, Z: 1}

part2_result = input
  .read
  .split("\n")
  .map {|m| m.split(" ")}
  .map {|m| m.map {|i| i.to_sym}}
  .map {|m| part2[m[1]] + ((part2_bonus[m[0]] + adj[m[1]]) % 3) + 1}
  .sum


puts "part2: #{part2_result}"
