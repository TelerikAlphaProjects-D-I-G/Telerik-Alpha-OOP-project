from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                output.append(self._process_command(input_line))
            except ValueError as err:
                output.append(err.args[0])

        print('\n\n'.join(str(item) for item in output))

    def _process_command(self, input_line):
        cmd, *params = input_line.split()

        return self._command_factory.create(cmd).execute(params)