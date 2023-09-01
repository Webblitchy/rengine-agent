# import whatportis
import subprocess
from os import rename, remove

from random import randint
from time import sleep

output_dir = "/usr/src/scan_results/"


def port_scanning(
    post_parameters,
) -> str:
    # Random sleep to prevent ip and port being overwritten
    sleep(randint(1, 5))
    """
    This function is responsible for running the port scan
    """
    port_results_file = f"{output_dir}{post_parameters['start_time']}-ports.json"

    # TODO: ?
    # domain_name = domain.name if domain else subdomain
    #
    # if domain:
    #     subdomain_scan_results_file = (
    #         "/usr/src/scan_results/sorted_subdomain_collection.txt"
    #     )
    #     naabu_command = "naabu -list {} -json -o {}".format(
    #         subdomain_scan_results_file, port_results_file
    #     )
    # elif subdomain:
    #     naabu_command = "naabu -host {} -o {}.tmp -json ".format(
    #         subdomain, port_results_file
    #     )
    # else:
    #     return "ERROR"

    IPs = ",".join(post_parameters["IPs"])
    naabu_command = "naabu -host {} -o {}.tmp -json ".format(IPs, port_results_file)

    # exclude cdn port scanning
    naabu_command += " -exclude-cdn "

    if post_parameters["include_ports"]:
        # TODO:  legacy code, remove top-100 in future versions
        if post_parameters["include_ports"] == "full":
            naabu_command += " -p -"
        elif post_parameters["include_ports"] == "top-100":
            naabu_command += " -top-ports 100 "
        elif post_parameters["include_ports"] == "top-1000":
            naabu_command += " -top-ports 1000 "
        else:
            naabu_command += " -p {} ".format(post_parameters["include_ports"])

    if post_parameters["exclude_ports"]:
        naabu_command += " -exclude-ports {} ".format(post_parameters["exclude_ports"])

    if post_parameters["rate"] != 0:
        naabu_command += " -rate {} ".format(post_parameters["rate"])

    if post_parameters["use_naabu_config"]:
        naabu_command += " -config /root/.config/naabu/config.yaml "

    # proxy = get_random_proxy()
    # if proxy:
    #     naabu_command += ' -proxy "{}" '.format(proxy)

    # run naabu
    # logger.info(naabu_command)
    print(naabu_command)
    process = subprocess.Popen(naabu_command.split())
    print("STARTING")
    process.wait()
    print("FINISHED")

    if process.returncode == 0:
        rename(
            port_results_file + ".tmp", port_results_file
        )  # remove the .tmp extention
        return "OK"
    else:
        print("Failed return code :", process.returncode)
        remove(port_results_file + ".tmp")
        return "ERROR"


def get_results(start_time: str):
    port_results_file = f"{output_dir}{start_time}-ports.json"
    try:
        with open(port_results_file, "r") as port_json_results:
            return port_json_results.read()
    except IOError:
        return "ERROR"
