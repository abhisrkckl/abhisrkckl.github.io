---
permalink: /software/
title: "Software"
---

# `pinta`
`pinta` is a data reduction pipeline for pulsar data taken using the upgraded [Giant Metre-wave Radio Telescope](https://gmrt.ncra.tifr.res.in/) (uGMRT).
It takes the uGMRT raw pulsar data as input, does RFI mitigation and folding, and gives partially folded profile archives as output.
It is now an [observatory pipeline at GMRT](http://www.ncra.tifr.res.in/ncra/gmrt/gmrt-users/pinta). 
This pipeline was described in [this paper](/publication/2021-04-14-pinta-paper).

[GitHub]((https://github.com/abhisrkckl/pinta))

# `ugmrt2fil`
`ugmrt2fil` is a program to convert uGMRT raw pulsar data to [sigproc](http://sigproc.sourceforge.net/)-filterbank format.
It is a part of the `pinta` pipeline.

[GitHub](https://github.com/abhisrkckl/ugmrt2fil)

# `GWecc`
`GWecc` is a library used to compute Pulsar Timing Array (PTA) signals due to gravitational waves emitted by black hole binaries. It is designed to be called from PTA data analysis packages like [`ENTERPRISE`](https://github.com/nanograv/enterprise). It can also be used to simulate pulsar time of arrivals using packages like [`libstempo`](https://github.com/vallis/libstempo) and [`PINT`](https://github.com/nanograv/PINT). 
This code is described in [this paper](/publication/2020-02-27-gwecc-paper).

[GitHub](https://github.com/abhisrkckl/gwecc)

# `mikkola`
This is an implementation of [Mikkola's method](https://doi.org/10.1007/BF01235850) for solving the classical [Kepler equation](https://en.wikipedia.org/wiki/Kepler%27s_equation). 

[GitHub](https://github.com/abhisrkckl/mikkola)
