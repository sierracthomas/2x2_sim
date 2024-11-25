from snewpy.neutrino import Flavor
from snewpy.models.ccsn import Fornax_2021
from astropy import units as u
from glob import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rc('font', size=16)
#%matplotlib inline


models = {}
for m in Fornax_2021.param['progenitor_mass'].value:#[::1]:
    # Initialise every second progenitor
    models[m] = Fornax_2021(progenitor_mass=m*u.solMass)

fig, axes = plt.subplots(4, 4, figsize=(12, 12), sharex=True, sharey=True, tight_layout=True)
times = []

my_models = models#([models[12], models[20]])
for i, model in enumerate(my_models.keys()):
    model = models[model]
    ax = axes.flatten()[i]
    for flavor in Flavor:
        ax.plot(model.time, model.luminosity[flavor]/1e51,  # Report luminosity in units foe/s
                label=flavor.to_tex(),
                color='C0' if flavor.is_electron else 'C1',
                ls='-' if flavor.is_neutrino else ':',
                lw=2)
    ax.set(xlim=(-0.05, 1.0),
           xlabel=r'$t-t_{\rm bounce}$ [s]',
           title=r'{} $M_\odot$'.format(model.metadata['Progenitor mass'].value))
    ax.grid()
    ax.legend(loc='upper right', ncol=2, fontsize=9)
    peak_time = model.time[np.argmax(model.luminosity[Flavor.NU_X])] # change flavor if you want the peak time of a different flavor
    ax.axvline(float(peak_time/u.s), color = "k")
    times.append(float(peak_time/u.s))
axes.flatten()[0].set(ylabel=r'luminosity [foe s$^{-1}$]');
plt.savefig("all_models_flux_rates.png")
plt.close()


times = np.array(times) * u.s
times
#model = models[12]  # Use the 12 solar mass model

#times = np.arange(-0.2, 3.8, 0.2) * u.s
E = np.arange(0, 101, 1) * u.MeV

fig, axes = plt.subplots(3,5, figsize=(15,10), sharex=True, sharey=True, tight_layout=True)

linestyles = ['-', '--', '-.', ':']

spectra = model.get_initial_spectra(times, E)


masses = np.array([*models.keys()])
#model_mass = model.metadata['Progenitor mass'].value


for i, ax in enumerate(axes.flatten()):
    #model = my_models[i]
    model = models[masses[i]]
    #print(model)
    for line, flavor in zip(linestyles, Flavor):
        #flavor = Flavor.NU_E
        ax.plot(E, spectra[flavor][i], lw=3, ls=line, label=flavor.to_tex())
        #espectrum = np.array([E, spectra[flavor][i]])
        #np.save(f"{model_mass}_NU_E_.npy", espectrum)
        normalize_factor = np.max(spectra[flavor][i])
        with open(f"{masses[i]}_{flavor}_hist.dat", "w") as myfile:
          for j in range(0, len(E)):
            myfile.write(f"{(E[j]/1000)/u.MeV} {spectra[flavor][i][j]/normalize_factor}\n")
    ax.set(xlim=(0,100)) 

    ax.set_title(f'{masses[i]} $M_\odot$, $t$ = {times[i]:.3f}', fontsize=16)
    ax.legend(loc='upper right', ncol=2, fontsize=12)

fig.text(0.5, 0., 'energy [MeV]', ha='center')
fig.text(0., 0.5, f'flux [{spectra[Flavor.NU_E].unit}]', va='center', rotation='vertical');
plt.savefig("all_models_energy_spectra.png")
plt.close()
