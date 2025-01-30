import random

ingredientes = ['Tomate', 'Piña', 'Jamón','Mozzarela', 'Masa']

ingrediente_random = random.choice(ingredientes) # Un único elemento
print(ingrediente_random) # 'Jamón'?

ingredientes_random = random.sample(ingredientes, 3) # Un subconjunto de n elementos no repetidos
print(ingredientes_random) # ['Mozzarela'?, 'Masa'?, 'Tomate'?]