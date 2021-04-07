#!/usr/bin/python
import jmespath

def normalize_version(version):
    # Return version and build number to be compared
    #20.1.4-9005-20210330.173606 : from Version file
    #20.1.4(9087) 2021-02-15 20:20:12 UTC : from API
    version = version.replace("(", "-")
    version = version.replace(")", "-")
    return (version.split("-")[0], version.split("-")[1])

class FilterModule(object):
    def filters(self):
        return {
            'upgrade_result': self.upgrade_result,
            'compare_versions': self.compare_versions
        }

    def upgrade_result(self, data):
        result = False
        data.setdefault('obj', {'results': []})
        upgrade_status = list(set(jmespath.search('[*].state.state', data['obj']['results'])))
        try:
            if len(upgrade_status) == 1 and upgrade_status[0] == "UPGRADE_FSM_COMPLETED":
                result = True
        except:
            pass
        return result

    def compare_versions(self, upgrade_version, controller_version):
        return normalize_version(upgrade_version) == normalize_version(controller_version)







