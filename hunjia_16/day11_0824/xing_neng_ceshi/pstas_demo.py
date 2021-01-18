
import cProfile
import pstats
def main():
    stats = pstats.Stats( "f:\\test.result")
    stats.sort_stats("time") #按照时间排序
    stats.print_stats()
if __name__ == '__main__':
    main()