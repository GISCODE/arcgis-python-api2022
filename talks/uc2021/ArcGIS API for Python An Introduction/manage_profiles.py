import os
import getpass
import argparse
import tempfile
import configparser
from typing import List, Dict, Any

from arcgis.gis import ProfileManager, GIS

__version__ = "Profile Manager Tools v1.0"

_PROFILEMANAGER = ProfileManager()
_DEFAULT_SECTIONS = frozenset(["your_online_profile", "your_enterprise_profile"])
###########################################################################
def create_profile(
    name: str, url: str = None, username: str = None, password: str = None
) -> bool:
    """Creates a Profile"""
    return _PROFILEMANAGER.create(
        profile=name, url=url, username=username, password=password
    )


# -------------------------------------------------------------------------
def update_profile(
    name: str, url: str = None, username: str = None, password: str = None
) -> bool:
    """updates an existing profile"""
    return _PROFILEMANAGER.update(
        profile=name, url=url, username=username, password=password
    )


# -------------------------------------------------------------------------
def delete_profile(name: str) -> bool:
    """deletes profile if it exists."""
    return _PROFILEMANAGER.delete(profile=name)


# -------------------------------------------------------------------------
def _section_info(config, section: str) -> Dict[str, str]:
    info = {}
    options = config.options(section)
    for option in options:
        try:
            val = config.get(section, option)
            if val == "":
                val = None
            info[option] = val
        except:
            info[option] = None

    return info


# -------------------------------------------------------------------------
def load_from_config(path: str) -> List[str]:
    """loads multiple configurations from a ini file"""
    config = configparser.ConfigParser()
    config.read(path)

    for profile in config.sections():
        info = _section_info(config, profile)
        if profile in list_profiles():
            update_profile(name=profile, **info)
        else:
            create_profile(name=profile, **info)
        del info, profile
    return list_profiles()


# -------------------------------------------------------------------------
def generate_configuration_file(
    save_folder: str, file_name: str = "profile_config.ini"
) -> str:
    """creates a profile configuration file for the user"""
    fp = os.path.join(save_folder, file_name)
    os.makedirs(save_folder, exist_ok=True)
    config = configparser.ConfigParser()
    with open(fp, "w") as cfgfile:
        for ds in _DEFAULT_SECTIONS:
            config.add_section(ds)
            for part in ["url", "username", "password"]:
                config.set(section=ds, option=part, value="")
        config.write(cfgfile)
    return fp


# -------------------------------------------------------------------------
def list_profiles() -> List[str]:
    """
    Lists the user profiles on the local machine

    :returns: List[str]
    """
    return _PROFILEMANAGER.list()


# -------------------------------------------------------------------------
def check_profile(name: str) -> Dict[str, Any]:
    """
    Returns Information about a Single Profile

    :return: Dict[str, Any]
    """
    if name in _PROFILEMANAGER.list():
        return _PROFILEMANAGER.get(name)
    return None


# -------------------------------------------------------------------------
def validate(name: str = "*") -> Dict[str, bool]:
    """validates all or a given profile"""
    passes = {}
    if name == "*":
        for p in _PROFILEMANAGER.list():
            try:
                gis = GIS(profile=p)
                del gis
                passes[p] = True
            except Exception as e:
                print(f"Profile {p} failed to connection with message: \n{e}")
                passes[p] = False
    else:
        try:
            gis = GIS(profile=name)
            del gis
            passes[name] = True
        except Exception as e:
            print(f"Profile {name} failed to connection with message: \n{e}")
            passes[name] = False
    return passes


# -------------------------------------------------------------------------
def main(
    action: str,
    profile: str = None,
    url: str = None,
    username: str = None,
    password: str = None,
    save_path: str = None,
    cfg: str = None,
    folder: str = None,
):
    """driver for the commandline tool."""
    print(
        "Welcome to the Profile Manager Tool\n"
        f"The following action is going to be performend: {action}"
    )
    try:

        if (
            action.lower() in ["add", "delete", "update", "get", "check"]
            and profile is None
        ):
            print("!!! A profile name is required !!!")
            raise ValueError("A profile must be provided when deleting a profile.")
        if action.lower() == "list":
            print("Registered Profiles: ")

            for profile in list_profiles():
                print(f"     - {profile}")
        elif action.lower() == "delete":
            if profile == "*":
                print(f"...Deleting... ")
                for p in list_profiles():
                    print(f"... Erasing {p} --> Completed {delete_profile(name=p)}")
            else:
                if profile in list_profiles():
                    print(f"...Deleting... ")
                    print(
                        f"... Erasing {profile} --> Completed {delete_profile(name=profile)}"
                    )
        elif action.lower() == "add":
            print(f"Adding the New Profile: {profile}")
            if url is None:
                print("The URL is set to ArcGIS Online by default.")
            if username is None:
                username = input("Enter your username: ")
            if password is None:
                password = getpass.getpass()

            res = create_profile(
                name=profile, url=url, username=username, password=password
            )
            print(f"... Profile {profile} added successfully: {res}")
        elif action.lower() == "update":
            print(f"Updating the Profile: {profile}")
            res = update_profile(
                name=profile, url=url, username=username, password=password
            )
            print(f"... Profile {profile} updated successfully: {res}")
        elif action.lower() in ["get", "check"]:
            if profile in list_profiles():
                print(f"... Obtaining the Profile: {profile}")
                print(check_profile(name=profile))
            else:
                print(f"... Profile {profile} not found.")
        elif action.lower() == "create" and save_path:
            print("... Generating the Configuration File ...")
            cfp = generate_configuration_file(save_folder=save_path)
            print(f"... File Located Here: {cfp} ...")
            print(
                "Update this file where the section in the square brackets [ ] is the "
                "name of the profile. The URL is only required for non-ArcGIS Online sites. "
                "The username and password should be provided.  Never share your configuration file."
            )
        elif action.lower() in ["load"]:
            if os.path.isfile(args.cfg):
                print(f"Loading the profiles from: {cfg}")
                print(load_from_config(path=args.cfg))
            else:
                raise ValueError(f"Cannot locate {cfg}")
        elif action.lower() == "validate":
            if profile is None:
                profile = "*"
            for k,v in validate(name=profile).items():
                print(f"   Profile {k} -- validated: {v}")
    except ValueError as ve:
        print(ve.args[0])
    finally:
        print("fin!")


# -------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to the Profile Manager.")
    parser.add_argument(
        "action",
        choices=[
            "add",
            "update",
            "delete",
            "list",
            "load",
            "check",
            "get",
            "create",
            "validate",
        ],
        help="action to be performed: add, update, list, delete, get",
    )

    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "--profile", default=None, type=str, help="The name of the profile"
    )
    parser.add_argument("--url", default=None, type=str, help="The URL of the site.")
    parser.add_argument(
        "--username", default=None, type=str, help="The username to login with"
    )
    parser.add_argument(
        "--password", default=None, type=str, help="The username password."
    )
    parser.add_argument(
        "--folder",
        default=tempfile.gettempdir(),
        type=str,
        help="The save path where the configuration file will be saved.",
    )
    parser.add_argument(
        "--cfg", default=None, type=str, help="The full path to the configuration file."
    )

    args = parser.parse_args()
    main(
        action=args.action,
        profile=args.profile,
        url=args.url,
        password=args.password,
        username=args.username,
        cfg=args.cfg,
        folder=args.folder,
    )
