start_times = []
end_times = []

n = int( raw_input() )
for i in xrange(n):
    racer_id, start_time, end_time = map(int, raw_input().split())
    data = (racer_id, start_time, end_time)
    start_times.append( data )
    end_times.append( data )

start_times.sort(key=lambda x: x[1], reverse=True)
end_times.sort(key=lambda x: x[2])

scores = []
for i in xrange(n):
    racer_id, start_time, end_time = start_times.pop()
    # binary search for ``end_time``
    l, h = 0, len(end_times)
    while l <= h:
        m = (l + h) / 2
        _, _, e = end_times[m]
        if end_time == e:
            scores.append( (m, racer_id) )
            end_times.pop(m)
            break
        elif end_time < e:
            h = m - 1
        elif end_time > e:
            l = m + 1

scores.sort()
for score, racer_id in scores:
    print racer_id, score
