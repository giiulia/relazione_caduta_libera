import numpy as np

#sfera 1
h1 = np.array([60.3, 60.2, 60.2, 60.3]) #in cm
h2 = np.array([58.4, 58.3, 58.3, 58.4])
h3 = np.array([55.6, 55.7, 55.8, 55.7])
h4 = np.array([50.4, 50.5, 50.4, 50.5])
h5 = np.array([45.0, 45.1, 45.0, 45.1])
h6 = np.array([39.5, 39.6, 39.7, 39.5])

tempo_caduta1 = np.array([0.3160, 0.3072, 0.3198, 0.3148, 0.3229, 0.3183, 0.3150, 0.3076, 0.3097, 0.3184]) #10 lanci misurati in s
tempo_caduta2 = np.array([0.3096, 0.3231, 0.3074, 0.3109, 0.3165, 0.3112, 0.3089, 0.3078, 0.2945, 0.3029])
tempo_caduta3 = np.array([0.2957, 0.3042, 0.2994, 0.3044, 0.2887, 0.2752, 0.3007, 0.2940, 0.2939, 0.2973])
tempo_caduta4 = np.array([0.2899, 0.2874, 0.2976, 0.2897, 0.2799, 0.2904, 0.2776, 0.2888, 0.2812, 0.2908])
tempo_caduta5 = np.array([0.2667, 0.2627, 0.2805, 0.2793, 0.2798, 0.2621, 0.2679, 0.2675, 0.2614, 0.2724])
tempo_caduta6 = np.array([0.2569, 0.2384, 0.2526, 0.2433, 0.2492, 0.2492, 0.2582, 0.2494, 0.2400, 0.2447])


#tempi e altezze
tempi = np.array([
    np.mean(tempo_caduta1),
    np.mean(tempo_caduta2),
    np.mean(tempo_caduta3),
    np.mean(tempo_caduta4),
    np.mean(tempo_caduta5),
    np.mean(tempo_caduta6)
])

altezze = np.array([
    np.mean(h1),
    np.mean(h2),
    np.mean(h3),
    np.mean(h4),
    np.mean(h5),
    np.mean(h6)
])