export INPUT="$1"

rm production/$INPUT_temp.mp3
rm production/$INPUT.mp3

ffmpeg -i music_effects/podcast_intro.mp3 -i originals/$INPUT.mp3 -filter_complex "[0:a][1:a]concat=n=2:v=0:a=1" production/$INPUT_temp.mp3
ffmpeg -i production/$INPUT_temp.mp3 -i music_effects/podcast_outro.mp3  -filter_complex "[0:a][1:a]concat=n=2:v=0:a=1" production/$INPUT.mp3

rm production/$INPUT_temp.mp3