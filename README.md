Задача
  Даны прямоугольники на плоскости с углами в целочисленных координатах ([1..109],[1..109]).
  Требуется как можно быстрее выдавать ответ на вопрос «Скольким прямоугольникам принадлежит точка (x,y)?» И подготовка данных должна занимать мало времени.
UPD: только нижние границы включены => (x1<= x) && (x<x2) && (y1<=y) && (y<y2)

1) Алгоритм перебора
Без подготовки. При поиске – просто перебор всех прямоугольников
Подготовка O(1), поиск O(N)
2) Алгоритм на карте
Сжатие координат и построение карты.
Подготовка O(N3), поиск O(logN)
3) Алгоритм на дереве
Сжатие координат и построение персистентного дерева отрезков 
Подготовка O(NlogN), поиск O(logN)
