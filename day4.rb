def split_pairs (pair)
  return pair.map {|e| e.split("-")}
end

def make_ints (pair)
  pair.map {|e| e.map {|r| r.to_i}}
end

def overlaps_p1? (pair)
  p1 = *(pair[0][0]..pair[0][1])
  p2 = *(pair[1][0]..pair[1][1])
  return (p2-p1).empty? || (p1-p2).empty?
end
  
# input = File.open("input")
#   .read
#   .split("\n")
#   .map {|p| p.split(",")}
#   .map {|p| split_pairs p}
#   .map {|p| make_ints p}
#   .map {|p| overlaps_p1? p}
#   .map {|p| p ? 1 : 0}
#   .sum

def overlaps_p2? (pair)
  p1 = *(pair[0][0]..pair[0][1])
  p2 = *(pair[1][0]..pair[1][1])
  return (p1 & p2).empty? ? 0 : 1
end
  
input = File.open("input")
  .read
  .split("\n")
  .map {|p| p.split(",")}
  .map {|p| split_pairs p}
  .map {|p| make_ints p}
  .map {|p| overlaps_p2? p}
  .sum

print input
