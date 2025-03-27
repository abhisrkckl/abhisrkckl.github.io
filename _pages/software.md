---
permalink: /software/
title: "Software"
---

# `PINT`
`PINT` is a pure-Python pulsar timing package. It has been used extensively for preparing the data releases of the NANOGrav and IPTA collaborations.
It is described in [this paper](https://ui.adsabs.harvard.edu/abs/2021ApJ...911...45L/abstract) and [this paper](https://ui.adsabs.harvard.edu/abs/2024ApJ...971..150S/abstract).

[GitHub](https://github.com/nanograv/PINT)

# `Vela.jl`
`Vela.jl` is a Bayesian pulsar timing & noise analysis package written in Julia and Python. It is described in 
[this paper](https://ui.adsabs.harvard.edu/abs/2025ApJ...980..165S/abstract).

[GitHub](https://github.com/abhisrkckl/Vela.jl)

# `GWecc.jl`
`GWecc.jl` is a Julia library used to compute Pulsar Timing Array (PTA) signals due to gravitational waves emitted by black hole binaries. 
It is designed to be called from PTA data analysis packages like [`ENTERPRISE`](https://github.com/nanograv/enterprise) and provides a Python binding for this purpose. 
It can also be used to simulate pulsar time of arrivals using packages like [`libstempo`](https://github.com/vallis/libstempo) and [`PINT`](https://github.com/nanograv/PINT). 
This code is based on [this paper](/publication/2020-02-27-gwecc) and [this paper](/publication/2022-10-21-gwecc-comput), and was applied in [this paper](/publication/2023-09-29-3c66b-gwecc-search).
It is a rewrite of the [GWecc](https://github.com/abhisrkckl/gwecc) code written in C++.

[GitHub](https://github.com/abhisrkckl/gwecc.jl)

# `pinta`
`pinta` is a data reduction pipeline for pulsar data taken using the upgraded [Giant Metre-wave Radio Telescope](https://gmrt.ncra.tifr.res.in/) (uGMRT).
It takes the uGMRT raw pulsar data as input, does RFI mitigation and folding, and gives partially folded profile archives as output.
It is now an [observatory pipeline at GMRT](http://www.ncra.tifr.res.in/ncra/gmrt/gmrt-users/pinta). 
This pipeline was described in [this paper](/publication/2021-04-14-pinta-paper).

[GitHub](https://github.com/inpta/pinta)

# `ugmrt2fil`
`ugmrt2fil` is a program to convert uGMRT raw pulsar data to [sigproc](http://sigproc.sourceforge.net/)-filterbank format.
It is a part of the `pinta` pipeline.

[GitHub](https://github.com/inpta/ugmrt2fil)

# `chimera`
`chimera` is a pipeline for creating wideband TOAs from CHIME pulsar observations. It is used for integrating CHIME data into NANOGrav.

[GitHub](https://github.com/abhisrkckl/chimera)

# `mikkola`
This is an implementation of [Mikkola's method](https://doi.org/10.1007/BF01235850) for solving the classical [Kepler equation](https://en.wikipedia.org/wiki/Kepler%27s_equation). 

[GitHub](https://github.com/abhisrkckl/mikkola)
