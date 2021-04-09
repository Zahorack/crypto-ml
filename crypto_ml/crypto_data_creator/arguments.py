class Args:
    use_std_coins: bool
    for_coins: []
    to_address: str
    data_policy: str

    def parse_args(self, args):
        for arg in args[1:]:
            [variable, value] = arg.split('=')

            if variable == 'for_coins':
                if value == 'supported':
                    self.use_std_coins = True
                else:
                    self.for_coins = value.split(',')
                    self.use_std_coins = False

            if variable == 'to_address':
                self.to_address = value

            if variable == 'data_policy':
                self.data_policy = value

    def __init__(self, args):
        self.parse_args(args)
