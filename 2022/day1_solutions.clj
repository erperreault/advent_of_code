(require '[clojure.string :as str])

(defn to_ints [str_vector]
  (map #(Integer/parseInt %) str_vector)
)

(defn sum_strs [str_vector]
  (reduce + (to_ints str_vector))
)

(defn get_elf_sum [str_vector]
  (sum_strs (str/split str_vector #"\n"))
)

(defn get_elves [str_vector]
  (str/split str_vector #"\n\n")
)

(defn part1 [input]
  (apply max (map get_elf_sum (get_elves input)))
)

(defn part2 [input]
  (reduce + (take 3 (sort > (map get_elf_sum (get_elves input)))))
)
