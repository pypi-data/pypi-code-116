#!/usr/bin/env python

"""Calculate scaffold domain occupancies for a simulation set"""


import argparse

import numpy as np

from origamipy import conditions
from origamipy import datatypes
from origamipy import files
from origamipy import outputs
from origamipy import utility


def main():
    args = parse_args()
    system_file = files.JSONStructInpFile(args.system_filename)
    staple_lengths = utility.calc_staple_lengths(system_file)
    inp_filebase = f"{args.outs_dir}/{args.filebase}"
    fileformatter = construct_fileformatter()
    reps_all_conditions = conditions.construct_mwus_conditions(
        args.windows_filename,
        args.bias_functions_filename,
        args.reps,
        args.run,
        args.temp,
        args.itr,
        args.staple_m,
        fileformatter,
        inp_filebase,
        staple_lengths,
        False,
    )
    sim_collections = []
    for rep in range(args.reps):
        rep_sim_collections = create_simplesim_collections(
            args, inp_filebase, rep, reps_all_conditions[rep]
        )
        sim_collections.append(rep_sim_collections)

    for rep_sim_collections in sim_collections:
        for sim_collection in rep_sim_collections:
            states_filename = "{}.states".format(sim_collection.filebase)
            states = np.loadtxt(states_filename)[:, : args.scaffold_domains]
            states = states == 2
            ops = datatypes.OrderParams.from_file(sim_collection.filebase)
            for i in range(args.scaffold_domains):
                tag = "domainstate{}".format(i)
                if tag in ops.tags:
                    ops[tag] = states[:, i]
                else:
                    ops.add_column(tag, states[:, i])

            out_filebase = sim_collection.filebase + "_mod"
            ops.to_file(out_filebase)


def construct_fileformatter():
    specs = [conditions.ConditionsFileformatSpec("bias", "{}")]
    return conditions.ConditionsFileformatter(specs)


def create_simplesim_collections(args, inp_filebase, rep, all_conds):
    sim_collections = []
    for conds in all_conds:
        filebase = f"{inp_filebase}_run-{args.run}_rep-{rep}{conds.fileformat}"
        sim_collection = outputs.SimpleSimCollection(filebase, conds)
        sim_collections.append(sim_collection)

    return sim_collections


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("system_filename", type=str, help="System file")
    parser.add_argument("filebase", type=str, help="Base name for files")
    parser.add_argument("outs_dir", type=str, help="outs directory")
    parser.add_argument("windows_filename", type=str, help="Windows filename")
    parser.add_argument(
        "bias_functions_filename", type=str, help="Bias functions filename"
    )
    parser.add_argument("temp", type=float, help="Temperature (K)")
    parser.add_argument("staple_m", type=float, help="Staple molarity (mol/V)")
    parser.add_argument("scaffold_domains", type=int, help="Number of scaffold domains")
    parser.add_argument("reps", type=int, help="Number of reps")
    parser.add_argument("run", type=int, help="Number of reps")
    parser.add_argument("itr", type=int, help="US iteration")

    return parser.parse_args()


if __name__ == "__main__":
    main()
