input = File.open("input")

# def priority (x)
#     first = x[0..(x.length/2)].split("")
#     second = x[(x.length/2)..(x.length+1)].split("")

#     seen = []
#     first.each do |i|
#       if not seen.include? i and second.include? i then
#         # return "#{i} #{i.ord} #{x[0..(x.length/2) - 1]}"
#         return i == i.upcase ? i.ord - 38 : i.ord - 96
#       end
#       seen.push(i)
#     end
# end

# p1_res = input
#   .read
#   .split("\n")
#   .map {|x| priority x}
#   .sum

# puts "part1: #{p1_res}"

def num_val (i)
  return i == i.upcase ? i.ord - 38 : i.ord - 96
end
  
groups = input.read.split("\n")
badges = []
i = 0
while i < groups.length do
  seen = []
  groups[i].split("").each do |c|
    if not seen.include? c and groups[i+1].include? c and groups[i+2].include? c then 
      badges.push(c)
      break
    end
    seen.push(c)
  end
  i += 3
end
print badges.map {|b| num_val b}.sum
