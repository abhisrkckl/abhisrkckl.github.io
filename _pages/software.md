---
permalink: /software/
title: "Software"
---

# `pinta`
[`pinta`](https://github.com/abhisrkckl/pinta) is a data reduction pipeline for pulsar data taken using the upgraded [Giant Metre-wave Radio Telescope](https://gmrt.ncra.tifr.res.in/) (uGMRT).
It takes the uGMRT raw pulsar data as input, does RFI mitigation and folding, and gives partially folded profile archives as output.
It will be commissioned as an observatory pipeline at GMRT soon. 
This pipeline was described in [this paper](/publication/2021-04-14-pinta-paper).

# `ugmrt2fil`
[`ugmrt2fil`](https://github.com/abhisrkckl/ugmrt2fil) is a program to convert uGMRT raw pulsar data to [sigproc](http://sigproc.sourceforge.net/)-filterbank format.
It is a part of the `pinta` pipeline.

# `GWecc`
[`GWecc`](https://github.com/abhisrkckl/gwecc) is a library used to compute Pulsar Timing Array (PTA) signals due to gravitational waves emitted by black hole binaries. It is designed to be called from PTA data analysis packages like [`ENTERPRISE`](https://github.com/nanograv/enterprise). It can also be used to simulate pulsar time of arrivals using packages like [`libstempo`](https://github.com/vallis/libstempo) and [`PINT`](https://github.com/nanograv/PINT). 
This code is described in [this paper](/publication/2020-02-27-gwecc-paper).

# `mikkola`
[This](https://github.com/abhisrkckl/mikkola) is an implementation of [Mikkola's method](https://doi.org/10.1007/BF01235850) for solving the classical [Kepler equation](https://en.wikipedia.org/wiki/Kepler%27s_equation). 
