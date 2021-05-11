import json
import yaml
from pathlib import Path

def filter_editable_text(pedurma_outline):
    editable_text = []
    for text_id, text in pedurma_outline.items():
        cur_text_info = {}
        if text['text_title'] and text['pedurma_title']:
            cur_text_info['p_id'] = text['rkts_id']
            cur_text_info['p_title'] = text['pedurma_title']
            cur_text_info['d_id'] = text['rkts_id']
            cur_text_info['d_title'] = text['text_title']
            if cur_text_info not in editable_text:
                editable_text.append(cur_text_info)
    return editable_text

if __name__ == "__main__":
    pedurma_outline = yaml.safe_load(Path('./pedurma_outline.yml').read_text(encoding='utf-8'))
    editable_text = filter_editable_text(pedurma_outline)
    print(f'Total {len(editable_text)} found editable..')
    Path('./t_text_list.json').write_text(json.dumps(editable_text, ensure_ascii=False), encoding='utf-8')
