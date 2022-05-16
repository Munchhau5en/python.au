При прочтении документации меня заинтересовала часть с воспроизведением изображений.

Я разобрался в коде и решил воспроизвести фотографию своей собаки

![](https://github.com/Munchhau5en/python.au/raw/main/Nika.jpg)

Код программы:

```python
import numpy
import imageio
import gari
import pygad
import matplotlib.pyplot


target_im = imageio.imread_v2('something.jpg')
target_im = numpy.asarray(target_im / 255, dtype=numpy.float64)


target_chromosome = gari.img2chromosome(target_im)


def fitness_fun(solution, solution_idx):
    fitness = numpy.sum(numpy.abs(target_chromosome - solution))

    fitness = numpy.sum(target_chromosome) - fitness
    return fitness


def callback(ga_instance):
    print("Generation = {gen}".format(gen=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))

    if ga_instance.generations_completed % 500 == 0:
        matplotlib.pyplot.imsave('solution_sth_' + str(ga_instance.generations_completed) + '.png',
                                 gari.chromosome2img(ga_instance.best_solution()[0], target_im.shape))


ga_instance = pygad.GA(num_generations=500,
                       num_parents_mating=10,
                       fitness_func=fitness_fun,
                       sol_per_pop=20,
                       num_genes=target_im.size,
                       init_range_low=0.0,
                       init_range_high=1.0,
                       mutation_percent_genes=0.01,
                       mutation_type="random",
                       mutation_by_replacement=True,
                       random_mutation_min_val=0.0,
                       random_mutation_max_val=1.0,
                       on_generation=callback)

ga_instance.run()


ga_instance.plot_fitness()


solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

if ga_instance.best_solution_generation != -1:
    print("Best fitness value reached after {best_solution_generation} generations.".format(
        best_solution_generation=ga_instance.best_solution_generation))

result = gari.chromosome2img(solution, target_im.shape)
matplotlib.pyplot.imshow(result)
matplotlib.pyplot.title("PyGAD & GARI for Reproducing Images")
matplotlib.pyplot.show()
```

Ситуация с собакой произошла максимально грустная, так как у фотографии слишком хорошее качество и обработка шла со скоростью ~14 поколений в минуту.

Обработка 20К поколений произошла бы спустя 24 часа непрерывной работы...
Извините, но моему компьютеру нужно отдыхать :(

Поэтому я чуть упростил себе задачу - нарисовал в пейнте два изображения - из 16 и 256 пикселей

Первое:

![](https://github.com/Munchhau5en/python.au/raw/main/something.jpg)

Второе:

![](https://github.com/Munchhau5en/python.au/raw/main/something_1.jpg)
