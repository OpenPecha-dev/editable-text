import json
import yaml
from pathlib import Path

def from_yaml(yml_path):
    return yaml.safe_load(yml_path.read_text(encoding="utf-8"))

def to_yaml(dict_):
    return yaml.safe_dump(dict_, sort_keys=False, allow_unicode=True)

def get_text_opf_id(text_id, text_opf_mapping):
    text_mapping = text_opf_mapping.get(text_id, {})
    if text_mapping:
        return text_mapping['uid']
    return ''

def get_text_mapping(pedurma_outline, editable_text_list):
    namsel_text_opf_mapping = from_yaml(Path('./namsel_text_opf_mapping.yml'))
    dg_text_opf_mapping = from_yaml(Path('./dg_text_opf_mapping.yml'))
    editable_text = {}
    for o_id, text in pedurma_outline.items():
        cur_text_info = {}
        text_id = text['rkts_id']
        if text_id in editable_text_list:
            cur_text_info['p_title'] = text['pedurma_title']
            # cur_text_info['namsel'] = get_text_opf_id(text_id, namsel_text_opf_mapping)
            # cur_text_info['google'] = get_text_opf_id(text_id, dg_text_opf_mapping)
            cur_text_info['namsel'] = "12d32eb31c1a4cc59741cda99ebc7211"
            cur_text_info['google'] = "187ed94f85154ea5b1ac374a651e1770"
            editable_text[text_id] = cur_text_info
    return editable_text

def parse_log_line(line):
    parts = line.split(' ')
    text_id = parts[2]
    uuid = parts[4]
    return text_id, uuid

def parse_log(log_file):
    text_mapping = {}
    log_lines = log_file.splitlines()
    for line in log_lines:
        text_id, uuid = parse_log_line(line)
        text_mapping[text_id] = uuid
    return text_mapping

if __name__ == "__main__":
    text_list = Path('./editable_textlist.txt').read_text(encoding='utf-8')
    editable_text_ids = text_list.splitlines()
    pedurma_outline = from_yaml(Path('./pedurma_outline.yml'))
    editable_text_mapping = get_text_mapping(pedurma_outline, editable_text_ids)
    editable_text_mapping = json.dumps(editable_text_mapping, ensure_ascii=False)
    Path('./text_pecha_mapping.json').write_text(editable_text_mapping)

