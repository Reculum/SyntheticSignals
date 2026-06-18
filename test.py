
from signal_class import *

def compute_snr(noise, *comps):

    noise_norm = np.linalg.norm(noise.get_image())

    S = signal(len(noise))

    for x in comps:
        S += x
    
    signal_norm = np.linalg.norm(S.get_image())

    return 20 * np.log10(signal_norm / noise_norm)



n = 2**10

snr_min_max = (20, 20)
beta_min_max = (0.5, 2)
T_min = 16

rnd_sign = signal(n)

(s, o, c, n) = rnd_sign.generate_blended_signal(snr_min_max, beta_min_max, T_min, prob_std_sin=0.1, kernel='cos')


print(f"SNR: {compute_snr(n, s, o, c)}")

print( f"error of the order: {np.log10(  np.max( np.abs( (s + o + c + n - rnd_sign).get_image() ) )   )}" )
#print( np.max( s.return_curvature_vect() ) )

plt.subplot(6, 1, 1)
plt.grid()
plt.plot(rnd_sign.get_image(), color='purple')

plt.subplot(6, 1, 2)
plt.grid()
plt.plot(s.get_image(), color='blue')

plt.subplot(6, 1, 3)
plt.grid()
plt.plot(o.get_image(), color='red')

plt.subplot(6, 1, 4)
plt.grid()
plt.plot(c.get_image(), color='green')

plt.subplot(6, 1, 5)
plt.grid()
plt.plot(n.get_image(), color='black')

plt.show()