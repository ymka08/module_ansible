#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result = dict(
        changed=False,
        path=path,
        content=content
    )

    if module.check_mode:
        module.exit_json(**result)

    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                current_content = file.read()
        else:
            current_content = None

        if current_content != content:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            result['changed'] = True

    except Exception as exc:
        module.fail_json(msg=str(exc), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
