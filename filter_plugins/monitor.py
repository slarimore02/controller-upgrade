#!/usr/bin/python
import jmespath

class FilterModule(object):
    def filters(self):
        return {
            'upgrade_result': self.upgrade_result,
            'get_gslb_upgrade_info': self.get_gslb_upgrade_info
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

    def get_gslb_upgrade_info(self, data):
        result = {}
        #Step One: Determine if mainteanance mode is enabled
        
        data.setdefault('obj', {'results': [{}]}) #Avoid KeyError
        result['maintenance_mode'] = data['obj']['results'].get('maintenance_mode', None)

        return result
        

