  self.bst.bft_print(self.bst)
        output = sys.stdout.getvalue()
        self.assertEqual(output, "1\n8\n5\n3\n7\n2\n4\n6\n")